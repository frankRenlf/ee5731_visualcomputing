# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/5 16:45 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
import cv2 as cv
import numpy as np

from skimage import feature, exposure


def test2():
    image = cv.imread('../data/img/img.png')
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 将图像转换为灰度图像
    fd, hog_image = feature.hog(gray_image, orientations=9, pixels_per_cell=(16, 16),
                                cells_per_block=(2, 2), visualize=True)
    # Rescale histogram for better display
    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
    while True:
        cv.imshow('img', image)
        cv.imshow('hog', hog_image_rescaled)
        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()


if __name__ == "__main__":
    test2()
