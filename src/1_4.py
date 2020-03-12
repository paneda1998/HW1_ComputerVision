import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('2.jpg',0)
img = cv2.GaussianBlur(img, (5, 5), 0)
canny_edge = cv2.Canny(img,200,400)
laplacian_edge = cv2.Laplacian(img,cv2.CV_64FC1)
sobelx_edge = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely_edge = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

sobelxx_edge = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobelyy_edge = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)
sobel  = sobelxx_edge+sobelyy_edge



laplacian = np.uint8(np.absolute(laplacian_edge))
sobelx = np.uint8(np.absolute(sobelx_edge))
sobely = np.uint8(np.absolute(sobely_edge))




plt.subplot(2,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,4),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,6),plt.imshow(sobel,cmap = 'gray')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3),plt.imshow(canny_edge,cmap = 'gray')
plt.title('canny'), plt.xticks([]), plt.yticks([])
plt.show()

