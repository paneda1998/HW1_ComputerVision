import numpy as np
import cv2

img = cv2.imread('2.jpg', 0)
width = 400
height = 300
img = cv2.resize(img, (400,300), interpolation=cv2.INTER_AREA)
high = cv2.Canny(img,100,200)
cv2.imshow("first high pass ",high)
kernel = np.ones((3, 3), np.float32) / (3 ** 2)
low_pass = cv2.filter2D(img, -1, kernel)

x_edge = np.zeros(img.shape, np.float)
y_edge = np.zeros(img.shape, np.float)
img = img.astype(dtype=np.float)

for i in range(300):
    for j in range(400):
        if (j == 400 - 1):
            y_edge[i, j] = -1 * img[i, j]
        else:
            y_edge[i, j] = img[i, j + 1] - img[i, j]

        if (i == 300 - 1):
            x_edge[i, j] = -1 * img[i, j]
        else:
            x_edge[i, j] = img[i + 1, j] - img[i, j]

y_edge = np.absolute(y_edge)
x_edge = np.absolute(x_edge)
y_edge = y_edge.astype(dtype=np.uint8)
x_edge = x_edge.astype(dtype=np.uint8)

# high frequency Filter.
# edge = sqrt(X_edge^2 + Y_edge^2)
edge = np.zeros(img.shape, np.float)
for i in range(300):
    for j in range(400):
        edge[i, j] = (x_edge[i, j] ** 2 + y_edge[i, j] ** 2) ** (1 / 2)
th2, edge = cv2.threshold(edge,30,255,cv2.THRESH_BINARY)
img = img.astype(dtype=np.uint8)
edge = edge.astype(dtype=np.uint8)

cv2.imshow('yEdge', y_edge)
cv2.imwrite("Y_edge.jpg" , y_edge)
cv2.imshow('xEdge', x_edge)
cv2.imwrite("X_edge.jpg" , x_edge)
cv2.imshow('UpFrequency', edge)
cv2.imwrite("UpFreq_output.jpg" , edge)
cv2.imshow('MainImage', img)
cv2.imshow('meanFilter', low_pass)
cv2.waitKey(0)
cv2.destroyAllWindows()
