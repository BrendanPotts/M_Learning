import numpy as np
import cv2


img = cv2.imread('face.jpg', cv2.IMREAD_COLOR)

if __name__=='__main__':

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_black = np.array([80,25,20])
    upper_black = np.array([255,200,160])

    mask = cv2.inRange(hsv, lower_black, upper_black)
    result = cv2.bitwise_and(img, img, mask=mask)


    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    