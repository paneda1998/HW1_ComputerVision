import cv2
import math
import tkinter
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

from scipy import ndimage

def nothing(x):
  pass
cv2.namedWindow('Rotation')
hh='Max'
hl='Min'
wnd = 'Rotation'
cv2.createTrackbar("Degree", "Rotation",0,360,nothing)


img= cv2.imread("space.jpg")
img1= cv2.imread("space.jpg",0)

height, width = img.shape[:2]
cv2.namedWindow('RGB', cv2.WINDOW_NORMAL)
cv2.resizeWindow('RGB', width, height)

while(1):
    cv2.imshow("RGB",img)
    a = cv2.getTrackbarPos("Degree", "Rotation")

    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        print(int(a))
        break
rotated = ndimage.rotate(img, a)
cv2.namedWindow('aaa', cv2.WINDOW_NORMAL)
cv2.resizeWindow('aaa', width, height)
cv2.imshow("aaa", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.subplot(1, 2, 1), plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(rotated)
plt.title('Rotated Image'), plt.xticks([]), plt.yticks([])
plt.show()
