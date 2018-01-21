import cv2
import numpy as np
from matplotlib import pyplot as plt


cap = cv2.VideoCapture(0)


if __name__=='__main__':
    while True:
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_color = np.array([80, 25, 20])
        upper_color = np.array([255, 200, 160])

        mask = cv2.inRange(hsv, lower_color, upper_color)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        k = cv2.waitKey(0) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
