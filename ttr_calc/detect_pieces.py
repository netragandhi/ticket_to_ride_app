import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from board_mapping import SEGMENT_SIZE, ROUTES, BOARD_CORNERS
from norm_points import NORM_POINTS, NORM_BOX_H, NORM_BOX_W

def align_images(empty_img, played_img):
    # Loads image as single channel grayscale
    empty_gray = cv.cvtColor(empty_img, cv.COLOR_BGR2GRAY)
    played_gray = cv.cvtColor(played_img, cv.COLOR_BGR2GRAY)

    # Initiate SIFT detector
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT, descriptor describes the pattern around the keypoint
    kp1, des1 = sift.detectAndCompute(empty_gray,None)
    kp2, des2 = sift.detectAndCompute(played_gray,None)
    # FLANN parameters, helps find similar descriptors quickly
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2) # returns 2 closest matches, first best and second best
    # ratio test as per Lowe's paper, removes false matches
    good = []

    for m,n in matches:
        if m.distance < 0.7*n.distance: # make sure that first best is much better than second best match to know that the match is actually correct, or we discard it
            good.append(m)

    # extracting the key points, converting to float32, restructing array to certain format
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)

    # finds the transformation and stores in matrix H
    H, mask = cv.findHomography(dst_pts, src_pts, cv.RANSAC, 5.0)

    # get empty image size
    h, w = empty_gray.shape

    # warp the played image to the size of the empty image
    aligned = cv.warpPerspective(played_img, H, (w, h))
    # cv.imshow("aligned", aligned)
    return aligned

def match_images(empty_img, aligned_img):
    empty_hsv = cv.cvtColor(empty_img, cv.COLOR_BGR2HSV).astype(np.float32)
    played_hsv = cv.cvtColor(aligned_img, cv.COLOR_BGR2HSV).astype(np.float32)

    h, w = empty_img.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)

    padding_px = 30
    w_seg_px = int(SEGMENT_SIZE[0] * w) + padding_px
    h_seg_px = int(SEGMENT_SIZE[1] * h) + padding_px

    for route_name, route in ROUTES.items():
        for seg in route["segments"]:
            cx = int(seg["center"][0] * w)
            cy = int(seg["center"][1] * h)
            angle = seg["angle"]

            mask = create_rotated_mask(mask, aligned_img.shape, (cx, cy), (w_seg_px, h_seg_px), angle)
    
    board_mask = np.zeros((h, w), dtype=np.uint8)
    pts = []
    for x_norm, y_norm in BOARD_CORNERS:
        x = int(x_norm * w)
        y = int(y_norm * h)
        pts.append([x, y])

    pts = np.array([pts], dtype=np.int32)
    cv.fillPoly(board_mask, pts, 255)

    # cv.imshow("mask", mask)
    background_mask = cv.bitwise_not(mask)
    # cv.imshow("backmask", background_mask)

    final_mask = cv.bitwise_and(board_mask, background_mask)
    cv.imshow("final", final_mask)

    # normalized_boxes = []
    # for cx, cy in NORM_POINTS:
    #     x1 = int((cx - NORM_BOX_W/2) * w)
    #     y1 = int((cy - NORM_BOX_H/2) * h)
    #     x2 = int((cx + NORM_BOX_W/2) * w)
    #     y2 = int((cy + NORM_BOX_H/2) * h)
    #     normalized_boxes.append((x1, y1, x2, y2))

    # for x1, y1, x2, y2 in normalized_boxes:
    #     mask[y1:y2, x1:x2] = 255

    for c in [1,2]:  # S=1, V=2
        template_vals = empty_hsv[:,:,c][background_mask==255]
        played_vals = played_hsv[:,:,c][background_mask==255]

        mean_t, std_t = template_vals.mean(), template_vals.std()
        mean_p, std_p = played_vals.mean(), played_vals.std()

        played_hsv[:,:,c] = (played_hsv[:,:,c] - mean_p) * (std_t / (std_p + 1e-6)) + mean_t
        played_hsv[:,:,c] = np.clip(played_hsv[:,:,c], 0, 255)
        print(f"Channel {c}")
        print(f"Template mean/std: {mean_t:.2f}, {std_t:.2f}")
        print(f"Played mean/std:   {mean_p:.2f}, {std_p:.2f}")
        print("-----")

    # H channel untouched
    played_norm = cv.cvtColor(played_hsv.astype(np.uint8), cv.COLOR_HSV2BGR)
    return played_norm

def create_rotated_mask(mask, board_shape, center_px, size_px, angle):
    rect = (center_px, size_px, angle)
    box = cv.boxPoints(rect).astype(int)
    cv.fillPoly(mask, [box], 255)
    return mask

def analyze_segment(empty_img, aligned_img, mask):
    empty_hsv = cv.cvtColor(empty_img, cv.COLOR_BGR2HSV).astype(np.float32)
    aligned_hsv = cv.cvtColor(aligned_img, cv.COLOR_BGR2HSV).astype(np.float32)

    # Color difference
    diff = cv.absdiff(empty_hsv, aligned_hsv)
    masked_diff = diff[mask == 255]
    color_diff = np.percentile(masked_diff[:,1:], 90)

    # 1. Structural Change (Canny Edges)
    # Catches pieces even if they are the same color as the board
    e1 = cv.Canny(cv.cvtColor(empty_img, cv.COLOR_BGR2GRAY), 50, 150)
    e2 = cv.Canny(cv.cvtColor(aligned_img, cv.COLOR_BGR2GRAY), 50, 150)
    edge_diff = np.mean(cv.absdiff(e1, e2)[mask == 255])

    # 3. Surface Texture (Variance)
    # Catches smooth vs. rough surface changes (good for shadows/reflections)
    tex_diff = abs(np.var(aligned_img[mask == 255]) - np.var(empty_img[mask == 255]))

    if color_diff > 100: # these def need to be changed and determined statistically
        occupied = True
        reason = "color"
    elif edge_diff > 60 or tex_diff > 1000:
        occupied = True
        reason = "edge/texture"
    else:
        occupied = False
        reason = "none"

    return occupied, color_diff, edge_diff, tex_diff, reason

def analyze_routes(empty_img, aligned_img, ROUTES):
    h, w = empty_img.shape[:2]
    results = {}
    w_seg_px = int(SEGMENT_SIZE[0] * w)
    h_seg_px = int(SEGMENT_SIZE[1] * h)

    for route_name, route in ROUTES.items():
        segment_results = []

        for seg in route["segments"]:
            cx = int(seg["center"][0] * w)
            cy = int(seg["center"][1] * h)
            angle = seg["angle"]
    
            blank_mask = np.zeros(empty_img.shape[:2], dtype=np.uint8)

            mask = create_rotated_mask(blank_mask, aligned_img.shape, (cx, cy), (w_seg_px, h_seg_px), angle)

            occupied, color_diff, edge_diff, tex_diff, reason = analyze_segment(empty_img, aligned_img, mask)

            segment_results.append({
                "center": (cx, cy),
                "angle": angle,
                "color_diff": color_diff,
                "edge_diff": edge_diff,
                "tex_diff": tex_diff,
                "reason": reason,
                "occupied": occupied
            })

        results[route_name] = segment_results
        
    return results

def visualize_segments(image, matched, ROUTES, results):
    vis = image.copy()
    vis_matched = matched.copy()
    h_img, w_img = image.shape[:2]
    w = int(SEGMENT_SIZE[0] * w_img)
    h = int(SEGMENT_SIZE[1] * h_img)

    # Draw your existing segment boxes
    for route_name, segs in results.items():
        for seg, seg_result in zip(ROUTES[route_name]["segments"], segs):
            cx, cy = seg_result["center"]
            angle = seg_result["angle"]

            rect = ((cx, cy), (w, h), angle)
            box = cv.boxPoints(rect).astype(int)

            color = (0, 0, 255) if seg_result["occupied"] else (0, 255, 0)
            cv.drawContours(vis, [box], 0, color, 2)
            cv.drawContours(vis_matched, [box], 0, color, 2)

    # for x, y in NORM_POINTS:
    #     # Calculate the actual pixel coordinates first
    #     x1 = int((x - NORM_BOX_W/2) * w_img)
    #     y1 = int((y - NORM_BOX_H/2) * h_img)
    #     x2 = int((x + NORM_BOX_W/2) * w_img)
    #     y2 = int((y + NORM_BOX_H/2) * h_img)

    #     # Now draw using the clean integer points
    #     cv.rectangle(vis, (x1, y1), (x2, y2), (255, 255, 255), 3)

    display = vis.copy()
    points = []

    def click_event(event, x, y, flags, param):
        nonlocal display

        if event == cv.EVENT_LBUTTONDOWN:
            # Normalize
            x_norm = x / w_img
            y_norm = y / h_img

            # print(f"Pixel: ({x}, {y})")
            # print(f"Normalized: ({x_norm:.4f}, {y_norm:.4f})")
            print(f'{{"center": ({x_norm:.4f}, {y_norm:.4f}), "angle": XXX}},')



            points.append((x_norm, y_norm))

            # Draw crosshair
            cv.line(display, (x-10, y), (x+10, y), (0,255,0), 1)
            cv.line(display, (x, y-10), (x, y+10), (0,255,0), 1)

            # Show normalized coords on image
            label = f"({x_norm:.3f},{y_norm:.3f})"
            cv.putText(display, label, (x+10, y-10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

            # Optional region box (also normalized)
            box_size = 40
            x1, y1 = x - box_size, y - box_size
            x2, y2 = x + box_size, y + box_size

            cv.rectangle(display, (x1, y1), (x2, y2), (255, 0, 0), 1)

            cv.imshow("Empty Display", display)

    cv.imshow("Played Display", vis_matched)
    cv.imshow("Empty Display", display)
    cv.setMouseCallback("Empty Display", click_event)

    while True:
        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv.destroyAllWindows()

empty_img = cv.imread('imgs/empty.jpeg')
played_img = cv.imread('imgs/played.jpeg')

aligned = align_images(empty_img, played_img)
matched = match_images(empty_img, aligned)
# diff_vis = cv.absdiff(aligned, matched)
# cv.imshow("Normalization Difference", diff_vis)
results = analyze_routes(empty_img, matched, ROUTES)

for route, segs in results.items():
    print(f"\nRoute: {route}")
    for i, s in enumerate(segs):
        print(f" Segment {i}: occupied={s['occupied']}, "
              f"color_diff={s['color_diff']:.2f}, edge_diff={s['edge_diff']:.2f}, "
              f"tex_diff={s['tex_diff']:.2f}, reason={s['reason']}")

visualize_segments(empty_img, matched, ROUTES, results)