import cv2
import numpy as np

img1 = cv2.imread('4.jpg',0)
img = cv2.imread('4.jpg')
# cv2.imshow("ss",img)
rows,cols = img1.shape
th, zero_one_img = cv2.threshold(img1, 80, 1, cv2.THRESH_BINARY_INV)

kernel = np.zeros((16,30))
kernel[0, :] = 1
kernel[15, :] = 1
kernel[:, 0] = 1
kernel[:, 29] = 1
filtered_img = cv2.filter2D(zero_one_img,-1,kernel)
th2, output = cv2.threshold(filtered_img, 72, 255, cv2.THRESH_BINARY)
pixels = np.argwhere(output == 255)
p = pixels
m, n = pixels.shape
for i in range(m):
    c = pixels[i][0]
    p[i][0] =pixels[i][1]
    p[i][1] = c
for x in range(m):
    final_output = cv2.circle(img, tuple(p[x]), 20, (0, 0, 255))


cv2.imshow('zero_one_img',zero_one_img)
cv2.imshow('filtered_img',filtered_img)
cv2.imshow('output',output)
cv2.imshow('final_output',final_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
