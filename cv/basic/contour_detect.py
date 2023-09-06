# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/6 14:24 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
import cv2 as cv
import numpy as np

if __name__ == "__main__":
    img = cv.imread('../data/img/1_cat.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gauss = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
    canny = cv.Canny(gauss, 125, 175)
    contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, -1, (0, 0, 255), 2)
    while True:
        cv.imshow('after', gauss)
        cv.imshow('origin', img)
        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()
