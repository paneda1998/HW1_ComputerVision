import cv2
a= cv2.imread("1.jpg")
b= cv2.imread("1.jpg",0)

height, width = a.shape[:2]
cv2.namedWindow('RGB', cv2.WINDOW_NORMAL)
cv2.resizeWindow('RGB', width, height)

cv2.namedWindow('grayscale', cv2.WINDOW_NORMAL)
cv2.resizeWindow('grayscale', width, height)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(a,'95101185',(10,1450), font, 1,(255,255,255),2)
cv2.putText(b,'95101185',(10,1450), font, 1,(255,255,255),2)

cv2.imshow("RGB",a)
cv2.imshow("grayscale",b)


k = cv2.waitKey(0)
if k == ord('e'):         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('RGB.jpg',a)
    cv2.imwrite('grayscale.jpg',b)
    cv2.destroyAllWindows()
