import numpy as np
import cv2 as cv
from detect_pieces import align_images, match_images, analyze_routes
from board_mapping import ROUTES

def collect_baseline_stats(empty_imgs, ROUTES):
    stats = []

    img1 = cv.imread('imgs/empty.jpeg')
    for i in range(len(empty_imgs)):
        img2 = empty_imgs[i]

        aligned = align_images(img1, img2)
        matched = match_images(img1, aligned)

        results = analyze_routes(img1, matched, ROUTES)

        for route, segs in results.items():
            for s in segs:
                stats.append([
                    s["color_diff"],
                    s["edge_diff"],
                    s["tex_diff"]
                ])

    stats = np.array(stats)
    return stats

def compute_thresholds(stats):
    mean = stats.mean(axis=0)
    std  = stats.std(axis=0)

    thr = mean + 3 * std   # 99.7% noise rejection

    print("Learned thresholds:")
    print(f"COLOR_THR = {thr[0]:.2f}")
    print(f"EDGE_THR  = {thr[1]:.2f}")
    print(f"TEX_THR   = {thr[2]:.2f}")

    return thr

empty_imgs = []
for i in range(1,10):
    empty_imgs.append(cv.imread(f'imgs/empty{i}.jpeg'))
stats = collect_baseline_stats(empty_imgs,ROUTES)
thr = compute_thresholds(stats)
print(thr)