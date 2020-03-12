import numpy as np
import cv2

cap = cv2.VideoCapture(0)
m = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        cap.release()
        cv2.destroyAllWindows()
        m = 2
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cap.release()
        cv2.destroyAllWindows()
        m = 1
        break
    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        cap.release()
        cv2.destroyAllWindows()
        m=2
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cap.release()
        cv2.destroyAllWindows()
        m=1
        break



# When everything done, release the captures


if m == 1:

    cap2 = cv2.VideoCapture(0)
    t = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter("cam.mp4", t, 20.0, (640, 480))
    while (1):
        ret1, frame1 = cap2.read()
        cv2.imshow('frame to be saved', frame1)
        output.write(frame1)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            cap2.release()
            output.release()
            cv2.destroyAllWindows()
            m = 5
            break


