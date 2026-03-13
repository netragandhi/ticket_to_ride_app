import numpy as np
import cv2 as cv

# Loads image as single channel grayscale
empty = cv.imread('imgs/empty.jpeg',cv.IMREAD_GRAYSCALE)
played = cv.imread('imgs/played.jpeg',cv.IMREAD_GRAYSCALE)

# Initiate SIFT detector
sift = cv.SIFT_create()
# find the keypoints and descriptors with SIFT, descriptor describes the pattern around the keypoint
kp1, des1 = sift.detectAndCompute(empty,None)
kp2, des2 = sift.detectAndCompute(played,None)
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
H, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)

# get empty image size
h, w = empty.shape

# warp the played image to the size of the empty image
aligned = cv.warpPerspective(played, H, (w, h))

# substract the played image from the empty image
diff = cv.absdiff(empty, aligned)

# converts image into black or white, white for the pieces, black for the board
_, thresh = cv.threshold(diff, 40, 255, cv.THRESH_BINARY)

# removes noise
kernel = np.ones((5,5),np.uint8)
thresh = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)

# detect boundaries of white regions (pieces)
contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# drawing bounding boxes
for c in contours:
    x,y,d_w,d_h = cv.boundingRect(c)
    cv.rectangle(aligned,(x,y),(x+d_w,y+d_h),(0,255,0),2)