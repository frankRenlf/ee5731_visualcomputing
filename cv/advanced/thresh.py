# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/8 18:41 
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
    # simple threshold
    threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
    threshold_inv, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
    # adaptive threshold
    thresh_adaptive = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
    thresh_adaptive_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
    thresh_adaptive_10 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 10)
    print(threshold, threshold_inv)
    while True:
        cv.imshow('gray', gray)
        cv.imshow('thresh', thresh)
        cv.imshow('thresh_inv', thresh_inv)
        cv.imshow('thresh_adaptive', thresh_adaptive)
        cv.imshow('thresh_adaptive_inv', thresh_adaptive_inv)
        cv.imshow('thresh_adaptive_10', thresh_adaptive_10)
        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()
