# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : visual_computing 
    @Product : PyCharm
    @createTime : 2023/9/4 22:53 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

import numpy as np
import cv2 as cv


# mouse callback function

class Draw:
    def __init__(self):
        self.mode = 0  # if True, draw rectangle. Press 'm' to toggle to curve
        self.drawing = False  # true if mouse is pressed
        self.ix, self.iy = -1, -1

    def draw_circle(self, event, x, y, flags, param):
        # global ix, iy, drawing, mode
        if event == cv.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix, self.iy = x, y
        elif event == cv.EVENT_MOUSEMOVE:
            if self.drawing:
                if self.mode == 0:
                    cv.rectangle(img, (self.ix, self.iy), (x, y), (0, 255, 0), thickness=cv.FILLED)
                elif self.mode == 1:
                    cv.circle(img, (x, y), 20, (0, 0, 255), thickness=2)
                elif self.mode == 2:
                    cv.putText(img, 'well done',
                               (x, y), cv.FONT_HERSHEY_COMPLEX,
                               0.5, (0, 0, 255), thickness=2)

        elif event == cv.EVENT_LBUTTONUP:
            self.drawing = False
            if self.mode == 0:
                cv.rectangle(img, (self.ix, self.iy), (x, y), (0, 255, 0), thickness=cv.FILLED)
            elif self.mode == 1:
                cv.circle(img, (x, y), 20, (0, 0, 255), 2)
            elif self.mode == 2:
                cv.putText(img, 'welldone',
                           (x, y), cv.FONT_HERSHEY_COMPLEX,
                           0.5, (0, 0, 255), thickness=2)


if __name__ == "__main__":
    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')
    draw = Draw()
    cv.setMouseCallback('image', draw.draw_circle)
    # print(cv.FILLED)
    while True:
        cv.imshow('image', img)
        k = cv.waitKey(1)
        if k == ord('m'):
            draw.mode = (draw.mode + 1) % 3
        elif k == ord('q'):
            break
    cv.destroyAllWindows()
