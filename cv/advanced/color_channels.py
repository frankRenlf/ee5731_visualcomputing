# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/6 14:57 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

import cv2 as cv
import numpy as np

if __name__ == "__main__":
    img = cv.imread('../data/img/1_cat.jpg')
    b, g, r = cv.split(img)
    bgr = cv.merge([r, g, b])
    while True:
        cv.imshow('after', bgr)
        cv.imshow('origin', img)
        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()
