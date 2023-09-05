# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/5 15:11 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
import numpy as np
import cv2 as cv
import sys


def transform():
    img = cv.imread('../data/img/1_cat.jpg')
    if img is None:
        sys.exit("Could not read the image.")

    arr = [img,
           cv.cvtColor(img, cv.COLOR_BGR2RGB),
           cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT),
           cv.Canny(cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT), 125, 127),
           cv.resize(img, (100, 100), interpolation=cv.INTER_AREA)]
    i = 0
    while True:
        k = cv.waitKey(1)
        if k == ord('0'):
            i = 0
        elif k == ord('1'):
            i = 1
        elif k == ord('2'):
            i = 2
        elif k == ord('3'):
            i = 3
        elif k == ord('4'):
            i = 4
        trans = arr[i]
        cv.imshow('img', trans)
        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()


if __name__ == "__main__":
    transform()
