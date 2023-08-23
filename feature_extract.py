# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : code 
    @Product : PyCharm
    @createTime : 2023/8/23 16:22 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""


def feature_extract(frameSize, features, feature) -> int:
    count = 0
    for i in range(features):
        size_x, size_y = feature[i]
        # print(size_x, size_y)
        for x in range(frameSize - size_x + 1):
            for y in range(frameSize - size_y + 1):
                for h in range(size_x, frameSize - x + 1, size_x):
                    for w in range(size_y, frameSize - y + 1, size_y):
                        count += 1
    return count


def feature_extract2(frameSize, features, feature) -> int:
    count = 0
    for i in range(features):
        size_x, size_y = feature[i]
        # print(size_x, size_y)
        for x in range(frameSize - size_x + 1):
            for y in range(frameSize - size_y + 1):
                count_x = (frameSize - x - size_x) // size_x + 1
                count_y = (frameSize - y - size_y) // size_y + 1
                count += count_x * count_y
    return count


if __name__ == "__main__":
    frameSize = 24
    features = 5
    feature = [[2, 1], [1, 2], [3, 1], [1, 3], [2, 2]]
    print(feature_extract2(24, 5, feature))
    print(feature_extract(24, 5, feature))
