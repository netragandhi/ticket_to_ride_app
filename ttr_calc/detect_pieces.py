import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

routes = {
    "miami_caracas": {
        "length": 2,
        "segment_size": (0.026, 0.016),  # width_ratio, height_ratio
        "segments": [
            {"center": (0.1832, 0.5099), "angle": 9},
            {"center": (0.1976, 0.5433), "angle": 85}  # positive = CCW
        ]
    },
        "daressalaam_djibouti": {
        "length": 1,
        "segment_size": (0.026, 0.016),  # width_ratio, height_ratio
        "segments": [
            {"center": (0.5462, 0.6217), "angle": 100}  # positive = CCW
        ]
    },
        "edinburgh_hamburg": {
        "length": 1,
        "segment_size": (0.026, 0.016),  # width_ratio, height_ratio
        "segments": [
            {"center": (0.4257, 0.2568), "angle": 9}  # positive = CCW
        ]
    }

}

normalized_points = [ # make these regions x1, y1, x2, y2
    (0.2336, 0.1875),
    (0.0378, 0.1068),
    (0.0339, 0.6547),
    (0.3330, 0.6456),
    (0.0874, 0.2132),
    (0.3312, 0.5181),
    (0.5897, 0.8226),
    (0.5730, 0.3159),
    (0.5894, 0.1994),
    (0.8857, 0.7680),
    (0.7315, 0.7873),
    (0.9581, 0.3691),
    (0.5087, 0.5938),
    (0.5170, 0.9188),
]

def align_images(empty_img, played_img):
    # Loads image as single channel grayscale
    empty_gray = cv.cvtColor(empty_img, cv.COLOR_BGR2GRAY)
    played_gray = cv.cvtColor(played_img, cv.COLOR_BGR2GRAY)

    h, w = empty_img.shape[:2]
    box_w = 0.01
    box_h = 0.01

    normalized_boxes = []
    for cx, cy in normalized_points:
        x1 = cx - box_w/2
        y1 = cy - box_h/2
        x2 = cx + box_w/2
        y2 = cy + box_h/2
        normalized_boxes.append((x1, y1, x2, y2))

    print(normalized_boxes) #visualize them
    # mask = np.zeros((h, w), dtype=np.uint8)

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
    cv.imshow("aligned", aligned)
    return aligned

# def find_corners(aligned_img)

#     return top_left_corner, top_right_corner, bot_left_corner 

def create_rotated_mask(board_shape, center_px, size_px, angle):
    mask = np.zeros(board_shape[:2], dtype=np.uint8)
    rect = (center_px, size_px, angle)
    box = cv.boxPoints(rect).astype(int)
    cv.fillPoly(mask, [box], 255)
    return mask

def analyze_segment(empty_img, aligned_img, mask):
    # Color difference
    diff = cv.absdiff(empty_img, aligned_img)
    masked_diff = diff[mask == 255]
    color_diff = np.percentile(masked_diff, 90)

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
    elif edge_diff > 25 or tex_diff > 800:
        occupied = True
        reason = "edge/texture"
    else:
        occupied = False
        reason = "none"

    return occupied, color_diff, edge_diff, tex_diff, reason

def analyze_routes(empty_img, aligned_img, routes):
    h_empty, w_empty = empty_img.shape[:2]
    results = {}

    for route_name, route in routes.items():
        w_seg_px = int(route["segment_size"][0] * w_empty)
        h_seg_px = int(route["segment_size"][1] * h_empty)
        segment_results = []

        for seg in route["segments"]:
            cx = int(seg["center"][0] * w_empty)
            cy = int(seg["center"][1] * h_empty)
            angle = seg["angle"]

            mask = create_rotated_mask(aligned_img.shape, (cx, cy), (w_seg_px, h_seg_px), angle)

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

def visualize_segments(image, routes, results):
    vis = image.copy()
    h_img, w_img = image.shape[:2]

    # Draw your existing segment boxes
    for route_name, segs in results.items():
        for seg, seg_result in zip(routes[route_name]["segments"], segs):
            cx, cy = seg_result["center"]
            w = int(routes[route_name]["segment_size"][0] * w_img)
            h = int(routes[route_name]["segment_size"][1] * h_img)
            angle = seg_result["angle"]

            rect = ((cx, cy), (w, h), angle)
            box = cv.boxPoints(rect).astype(int)

            color = (0, 0, 255) if seg_result["occupied"] else (0, 255, 0)
            cv.drawContours(vis, [box], 0, color, 2)

    display = vis.copy()
    points = []

    def click_event(event, x, y, flags, param):
        nonlocal display

        if event == cv.EVENT_LBUTTONDOWN:
            # 🔥 Normalize
            x_norm = x / w_img
            y_norm = y / h_img

            print(f"Pixel: ({x}, {y})")
            print(f"Normalized: ({x_norm:.4f}, {y_norm:.4f})")

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

            cv.imshow("Segment Visualization", display)

    cv.imshow("Segment Visualization", display)
    cv.setMouseCallback("Segment Visualization", click_event)

    while True:
        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv.destroyAllWindows()

empty_img = cv.imread('imgs/empty.jpeg')
played_img = cv.imread('imgs/played2.jpeg')

aligned = align_images(empty_img, played_img)
results = analyze_routes(empty_img, aligned, routes)

for route, segs in results.items():
    print(f"\nRoute: {route}")
    for i, s in enumerate(segs):
        print(f" Segment {i}: occupied={s['occupied']}, "
              f"color_diff={s['color_diff']:.2f}, edge_diff={s['edge_diff']:.2f}, "
              f"tex_diff={s['tex_diff']:.2f}, reason={s['reason']}")

visualize_segments(empty_img, routes, results)