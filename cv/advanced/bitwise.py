# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/6 15:29 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

import cv2 as cv
import numpy as np

if __name__ == "__main__":
    img = cv.imread('../data/img/1_cat.jpg')
    blank = np.zeros((400, 400), dtype='uint8')
    img1 = cv.rectangle(blank.copy(), (30, 30), (370, 370), (255, 255, 255), -1)
    img2 = cv.circle(blank.copy(), (200, 200), 200, (255, 255, 255), -1)
    bitwise_and = cv.bitwise_and(img1, img2)
    bitwise_or = cv.bitwise_or(img1, img2)
    bitwise_xor = cv.bitwise_xor(img1, img2)

    img_crop1 = img[0:200, 0:200]
    img_crop2 = img[100:300, 100:300]
    img_xor = cv.bitwise_xor(img_crop1, img_crop2)
    while True:
        cv.imshow('rectangle', img1)
        cv.imshow('circle', img2)
        cv.imshow('bitwise_and', bitwise_and)
        cv.imshow('bitwise_or', bitwise_or)
        cv.imshow('bitwise_xor', bitwise_xor)
        cv.imshow('img_xor', img_xor)
        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()
