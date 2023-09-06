# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/5 13:42 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
import cv2 as cv
import numpy as np


def exchange_():
    cap = cv.VideoCapture(0)

    while (1):

        # Take each frame
        _, frame = cap.read()

        # Convert BGR to HSV
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_blue = np.array([50, 50, 50])
        upper_blue = np.array([255, 255, 255])

        # Threshold the HSV image to get only blue colors
        mask = cv.inRange(hsv, lower_blue, upper_blue)

        # Bitwise-AND mask and original image
        res = cv.bitwise_and(frame, frame, mask=mask)

        cv.imshow('frame', frame)
        cv.imshow('mask', mask)
        cv.imshow('res', res)
        k = cv.waitKey(1)
        if k == ord('q'):
            break

    cv.destroyAllWindows()


if __name__ == "__main__":
    exchange_()
