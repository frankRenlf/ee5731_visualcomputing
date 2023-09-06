# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/6 15:52 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
import cv2 as cv
import numpy as np

if __name__ == "__main__":
    img = cv.imread('../data/img/1_cat.jpg')
    blank = np.zeros(img.shape[:2], dtype='uint8')
    rec = cv.rectangle(blank.copy(), (50, 50,), (200, 200), (255, 255, 255), -1)
    aft = cv.bitwise_and(img, img, mask=rec)
    while True:

        cv.imshow('img', img)
        cv.imshow('aft', aft)
        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()
