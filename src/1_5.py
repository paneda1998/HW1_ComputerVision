import cv2
import math
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage


img= cv2.imread("limbo.png",0)
height, width = img.shape[:2]
cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
cv2.resizeWindow('gray', width, height)
kernel = np.ones((3,3),np.uint8)
# erosion = cv2.erode(img,kernel,iterations = 1)
# dilation = cv2.dilate(img,kernel,iterations = 1)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


cv2.imshow("gray",img)
cv2.imshow("opening",closing)
k = cv2.waitKey(0)
if k == ord('e'):         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('closing3.png',closing)
    # cv2.imwrite('grayscale.jpg',b)
    cv2.destroyAllWindows()
