# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/6 14:45 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    img = cv.imread('../data/img/1_cat.jpg')
    plt.imshow(img)
    # plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.show()
    while True:
        # cv.imshow('after', gauss)
        cv.imshow('origin', img)
        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()
