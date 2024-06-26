# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/5 13:04 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import sys

if __name__ == "__main__":
    BLUE = [255, 0, 0]

    img1 = cv.imread("../data/img/1_cat.jpg")

    replicate = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REPLICATE)
    reflect = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT)
    reflect101 = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
    wrap = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_WRAP)
    constant = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=BLUE)

    plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
    plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
    plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
    plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
    plt.show()


