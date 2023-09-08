# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/8 19:09 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    img = cv.imread('../data/img/1_cat.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # laplacian
    lap = cv.Laplacian(gray, cv.CV_64F)
    lap_display = np.uint8(np.absolute(lap))
    # sobel
    sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
    sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
    sobel = cv.Sobel(gray, cv.CV_64F, 1, 1)
    sobel_xy = cv.bitwise_or(sobel_x, sobel_y)

    while True:
        cv.imshow('gray', gray)
        cv.imshow('lap_display', lap_display)
        cv.imshow('sobel_x', sobel_x)
        cv.imshow('sobel_y', sobel_y)
        cv.imshow('sobel', sobel)
        cv.imshow('sobel_xy', sobel_xy)

        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()
