# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/5 13:30 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : mixture
"""
import cv2 as cv


def mix_():
    img1 = cv.imread('../data/img/1_cat.jpg')
    img2 = cv.imread('../data/img/banana.jpg')
    img1.resize((256, 256, 3))
    dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)
    print(img1.shape, img2.shape)
    cv.imshow('dst', dst)
    cv.imshow('1', img1)
    cv.waitKey(0)
    cv.destroyAllWindows()


def mix_2():
    img1 = cv.imread('../data/img/1_cat.jpg')
    img2 = cv.imread('../data/img/banana.jpg')

    # I want to put logo on top-left corner, So I create a ROI
    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]

    # Now create a mask of logo and create its inverse mask also
    img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)

    # Now black-out the area of logo in ROI
    img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

    # Take only region of logo from logo image.
    img2_fg = cv.bitwise_and(img2, img2, mask=mask)

    # Put logo in ROI and modify the main image
    dst = cv.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols] = dst
    cv.imshow('1bg', img1_bg)
    cv.imshow('2fg', img2_fg)
    cv.imshow('res', img1)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    mix_2()
