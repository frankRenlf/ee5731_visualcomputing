# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : pytorch 
    @Product : PyCharm
    @createTime : 2023/8/16 17:58 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

import numpy as np
import cv2 as cv


def camera_read():
    cap = cv.VideoCapture(0)

    size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    out = cv.VideoWriter('../data/video/output.mp4', fourcc, 15, size)

    face_cascade = cv.CascadeClassifier(
        '/Users/frank/anaconda3/envs/d2l-zh/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # write the flipped frame
        frame = cv.flip(frame, 1)
        # 将图像转换为灰度图像（Haar Cascade通常要求灰度图像）
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 使用Haar Cascade进行人脸检测
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        # 在检测到的人脸周围绘制矩形框
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()


def changeRes(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)


def read_video():
    cap = cv.VideoCapture(1)
    # changeRes(cap, 1280, 720)s
    size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
    print(size)
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    out = cv.VideoWriter('../data/video/output3.mp4', fourcc, 15, size)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # write the flipped frame
        frame = cv.flip(frame, 1)
        out.write(frame)
        cv.imshow('frame', frame)
        # cv.imshow('frame_resize',
        #           cv.resize(frame,
        #                     (int(frame.shape[1] * 0.75), int(frame.shape[0] * 0.75)),
        #                     interpolation=cv.INTER_AREA)
        #           )
        if cv.waitKey(1) == ord('q'):
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    camera_read()


