import cv2
a= cv2.imread("football.jpg")


height, width = a.shape[:2]
cv2.namedWindow('RGB', cv2.WINDOW_NORMAL)
cv2.resizeWindow('RGB', width, height)

b = cv2.rectangle(a, (290, 455), (380, 531), (0, 255, 0), 3)
roi = a[455:531,290:380]
a[455:531,590:680] = roi
cv2.imshow("RGB",a)

cv2.imwrite('newfootball.jpg', a)

cv2.waitKey(0)
cv2.destroyAllWindows()
