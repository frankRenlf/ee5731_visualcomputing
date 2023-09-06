# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/6 10:25 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
import cv2 as cv
import numpy as np


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)


def rotate(img, angle, rotatePoint=None):
    height, weight = img.shape[:2]
    if rotatePoint is None:
        rotatePoint = [weight / 2, height / 2]
    dimension = (weight, height)
    transMat = cv.getRotationMatrix2D(rotatePoint, angle, 1.0)
    return cv.warpAffine(img, transMat, dimension)


if __name__ == "__main__":
    img = cv.imread('../data/img/1_cat.jpg')
    trans = translate(img, -100, 100)
    rotation = rotate(img, 45, )
    while True:
        cv.imshow('img', rotation)
        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()
