import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

routes = {
    "test_route": {
        "length": 2,
        "segment_size": (0.026, 0.016),  # width_ratio, height_ratio
        "segments": [
            {"center": (0.185, 0.51), "angle": 8},
            {"center": (0.199, 0.54), "angle": 85}  # positive = CCW
        ]
    }
}

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
    cv.imshow("aligned", aligned)
    return aligned

def create_rotated_mask(board_shape, center_px, size_px, angle):
    mask = np.zeros(board_shape[:2], dtype=np.uint8)
    rect = (center_px, size_px, angle)
    box = cv.boxPoints(rect).astype(int)
    cv.fillPoly(mask, [box], 255)
    return mask

def analyze_segment(empty_region, aligned_region):
    # 1. Structural Change (Canny Edges)
    # Catches pieces even if they are the same color as the board
    e1 = cv.Canny(cv.cvtColor(empty_region, cv.COLOR_BGR2GRAY), 50, 150)
    e2 = cv.Canny(cv.cvtColor(aligned_region, cv.COLOR_BGR2GRAY), 50, 150)
    edge_score = np.mean(cv.absdiff(e1, e2))

    # 2. Color Intensity (Saturation)
    # Catches brightly colored pieces on dull backgrounds
    hsv = cv.cvtColor(aligned_region, cv.COLOR_BGR2HSV)
    sat_score = np.mean(hsv[:, :, 1])

    # 3. Surface Texture (Variance)
    # Catches smooth vs. rough surface changes (good for shadows/reflections)
    tex_score = np.var(aligned_region)

    # 4. Overall Brightness Change (Value)
    # Helps detect shadows or highlights created by a new object
    val_score = np.mean(hsv[:, :, 2])
    empty_val = np.mean(cv.cvtColor(empty_region, cv.COLOR_BGR2HSV)[:, :, 2])
    brightness_diff = abs(empty_val - val_score)

    return edge_score, sat_score, tex_score, brightness_diff

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
            empty_region = cv.bitwise_and(empty_img, empty_img, mask=mask)
            aligned_region = cv.bitwise_and(aligned_img, aligned_img, mask=mask)

            edge_score, sat_score, tex_score, brightness_diff = analyze_segment(empty_region, aligned_region)
            occupied = edge_score > 15 or sat_score > 50 or tex_score > 500 or brightness_diff > 20

            segment_results.append({
                "center": (cx, cy),
                "angle": angle,
                "edge_score": edge_score,
                "sat_score": sat_score,
                "tex_score": tex_score,
                "brightness_diff": brightness_diff,
                "occupied": occupied
            })

        results[route_name] = segment_results
    return results

def visualize_segments(image, routes, results):
    vis = image.copy()
    for route_name, segs in results.items():
        for seg, seg_result in zip(routes[route_name]["segments"], segs):
            cx, cy = seg_result["center"]
            w = int(routes[route_name]["segment_size"][0] * image.shape[1])
            h = int(routes[route_name]["segment_size"][1] * image.shape[0])
            angle = seg_result["angle"]

            rect = ((cx, cy), (w, h), angle)
            box = cv.boxPoints(rect).astype(int)

            color = (0, 0, 255) if seg_result["occupied"] else (0, 255, 0)
            cv.drawContours(vis, [box], 0, color, 2)

    cv.imshow("Segment Visualization", vis)
    cv.waitKey(0)
    cv.destroyAllWindows()


empty_img = cv.imread('imgs/empty.jpeg')
played_img = cv.imread('imgs/played.jpeg')

aligned = align_images(empty_img, played_img)
results = analyze_routes(empty_img, aligned, routes)

for route, segs in results.items():
    print(f"\nRoute: {route}")
    for i, s in enumerate(segs):
        print(f" Segment {i}: occupied={s['occupied']}, "
              f"edge={s['edge_score']:.2f}, sat={s['sat_score']:.2f}, "
              f"tex={s['tex_score']:.2f}, bright_diff={s['brightness_diff']:.2f}")

visualize_segments(aligned, routes, results)




# cv.imshow("Aligned", aligned)
# cv.imshow("Diff", diff)
# cv.imshow("Threshold", thresh)
# cv.waitKey(0)

# plt.imshow(aligned, cmap='gray')

# def onclick(event):
#     print(int(event.xdata), int(event.ydata))

# plt.connect('button_press_event', onclick)
# plt.show()
