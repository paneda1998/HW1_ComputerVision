import numpy as np
import cv2
Video = cv2.VideoCapture('video.mp4')
gray_img = cv2.imread('background.jpg',0)

width = int(Video.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(Video.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('gray_video.mp4', fourcc, 10, (1920, 1080),False)
while(1):
    ret, frame = Video.read()
    if ret==True:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        outputt = gray_frame - gray_img
        th, dst = cv2.threshold(outputt, 5, 255, cv2.THRESH_BINARY_INV)

        cv2.imshow('frame',dst)
        out.write(dst)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if ret == False:
        break

Video.release()
out.release()
cv2.destroyAllWindows()
