# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/6 15:08 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : remove some noise
"""

import cv2 as cv
import numpy as np

if __name__ == "__main__":
    img = cv.imread('../data/img/1_cat.jpg')
    medianBlur = cv.medianBlur(img, 7)
    while True:
        cv.imshow('after', medianBlur)
        cv.imshow('origin', img)
        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()
