# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/12 15:56 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
from stitching import Stitcher, AffineStitcher

if __name__ == "__main__":
    # stitcher = Stitcher(detector="sift", confidence_threshold=0.2)
    # panorama = stitcher.stitch(['./img/box.png', './img/box_in_scene.png'])
    stitcher2 = AffineStitcher()
    panorama2 = stitcher2.stitch(['./img/box.png', './img/box_in_scene.png'])
