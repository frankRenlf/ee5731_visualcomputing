# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : pytorch 
    @Product : PyCharm
    @createTime : 2023/8/16 17:45 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : first
"""

import cv2 as cv
import sys
import numpy as np


def sift_demo():
    # 读取图像
    image_path = '../data/img/1_cat.jpg'
    image = cv.imread(image_path)

    # 创建HOG描述符计算器
    win_size = (32, 64)
    block_size = (8, 8)
    block_stride = (4, 4)
    cell_size = (4, 4)
    nbins = 9
    hog = cv.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)

    # 计算HOG特征
    hog_features = hog.compute(image)

    # 获取HOG特征方向图和可视化
    num_cells_x = (image.shape[1] // cell_size[0])
    num_cells_y = (image.shape[0] // cell_size[1])
    num_blocks_x = (num_cells_x - block_size[0] // cell_size[0] + 1)
    num_blocks_y = (num_cells_y - block_size[1] // cell_size[1] + 1)
    hog_image = np.zeros((num_cells_y, num_cells_x))

    for y in range(num_cells_y):
        for x in range(num_cells_x):
            block_idx = (x // block_stride[0], y // block_stride[1])
            cell_idx = (x % block_stride[0] // cell_size[0], y % block_stride[1] // cell_size[1])
            hist_start_idx = (block_idx[1] * num_blocks_x + block_idx[0]) * nbins
            hist_idx = hist_start_idx + cell_idx[1] * (block_size[0] // cell_size[0]) + cell_idx[0]
            hog_image[y, x] = hog_features[hist_idx]

    hog_image = hog_image / np.max(hog_image) * 255  # 线性映射到 [0, 255] 范围
    hog_image = hog_image.astype(np.uint8)

    # 显示图像和HOG方向图
    cv.imshow('Image', image)
    cv.imshow('HOG Direction Image', hog_image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    img = cv.imread(cv.samples.findFile("../data/img/1_cat.jpg"))
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow("Display window", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("../data/img/banana_3.jpg", img)
