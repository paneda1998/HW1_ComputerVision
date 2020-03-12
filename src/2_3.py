import numpy as np
import cv2
import math

cap = cv2.VideoCapture('cam.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('prewitty_edge.mp4',fourcc, 20.0, (640,480), False)
# laplacian_edge = cv2.Laplacian(img,cv2.CV_64FC1)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Gaussian Filter
        frame = cv2.GaussianBlur(frame, (5, 5), 0)
        #canny edge detector
        c_img = cv2.Canny(frame, 50, 100)
        #sobel edge detector
        sobelx_edge = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=5)
        sobely_edge = cv2.Sobel(frame, cv2.CV_8U, 0, 1, ksize=5)
        sobel_img  = sobelx_edge+sobely_edge
        #prewitt edge detector
        kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        img_prewittx = cv2.filter2D(frame, -1, kernelx)
        img_prewitty = cv2.filter2D(frame, -1, kernely)
        prewitt_img = img_prewittx + img_prewitty
        
        out.write(prewitt_img)
        cv2.imshow('frame',prewitt_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
           break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
