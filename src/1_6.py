import cv2
import numpy as np

# Read image
im = cv2.imread("3.jpg", cv2.IMREAD_GRAYSCALE)
# params.maxArea = 2000

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 20
params.maxThreshold = 255
# Filter by Area.
params.filterByArea = True
params.minArea = 800
params.maxArea = 4000
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = .7
params.maxCircularity = 1
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = .7
params.maxConvexity = 1
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.8
params.maxInertiaRatio = 1


detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
