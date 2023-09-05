# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/5 11:30 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

import numpy as np
import cv2 as cv
from intro_mouse_draw import Draw


def nothing(x):
    pass


def adjust():
    # Create a black image, a window
    img = np.zeros((300, 512, 3), np.uint8)
    cv.namedWindow('image')
    draw = Draw()

    # create trackbars for color change
    cv.createTrackbar('R', 'image', 0, 255, nothing)
    cv.createTrackbar('G', 'image', 0, 255, nothing)
    cv.createTrackbar('B', 'image', 0, 255, nothing)

    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv.createTrackbar(switch, 'image', 0, 1, nothing)
    cv.setMouseCallback('image', draw.draw_circle)

    while 1:
        cv.imshow('image', img)
        k = cv.waitKey(1)

        if k == ord('m'):
            draw.mode = not draw.mode

        if k == ord('q'):
            break

        # get current positions of four trackbars
        r = cv.getTrackbarPos('R', 'image')
        g = cv.getTrackbarPos('G', 'image')
        b = cv.getTrackbarPos('B', 'image')
        s = cv.getTrackbarPos(switch, 'image')
        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]

    cv.destroyAllWindows()


if __name__ == "__main__":
    adjust()
