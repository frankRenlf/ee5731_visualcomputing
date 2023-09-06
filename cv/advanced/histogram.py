# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/6 16:05 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : histogram
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    img = cv.imread('../data/img/1_cat.jpg')
    blank = np.zeros(img.shape[:2], dtype='uint8')
    print(blank.shape)
    rec1 = cv.rectangle(blank.copy(), (400, 0), (500, 400), (255, 255, 255), -1)
    rec2 = cv.rectangle(blank.copy(), (200, 100), (370, 150), (255, 255, 255), -1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    mask_rec2 = cv.bitwise_and(gray, gray, mask=rec2)
    mask_rec1 = cv.bitwise_and(gray, gray, mask=rec1)
    hist1 = cv.calcHist([rec1], [0], None, [180], [0, 256])
    hist2 = cv.calcHist([rec2], [0], None, [180], [0, 256])
    # hist_gray = cv.calcHist([gray], [0], mask_rec1, [360], [0, 256])

    gray_crop = gray[100:150, 200:370]
    hist_gray = cv.calcHist([gray_crop], [0], None, [256], [0, 256])

    plt.figure()
    # plt.subplot()
    # plt.plot(hist1)
    # plt.subplot()
    plt.plot(hist_gray)

    plt.show()

    # while True:
    #     cv.imshow('rec1', mask_rec1)
    #     cv.imshow('rec2', mask_rec2)
    #     cv.imshow('gray_crop', gray_crop)
    #     if cv.waitKey(1) == ord('q'):
    #         break
    cv.destroyAllWindows()
