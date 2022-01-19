import os
from urllib.request import urlopen

import cv2
import numpy as np
from pytube import YouTube


def download(download_link, filename):
    if not os.path.exists(filename):
        print(f"Downloading video '{filename}' from '{download_link}' ...")
        rsp = urlopen(download_link)
        with open(filename, 'wb') as f:
            f.write(rsp.read())
        print("Download finish!")


def download_youtube(download_link, filename, file_extension):
    if not os.path.exists(filename):
        print(f"Downloading Youtube video '{filename}' from '{download_link}' "
              f"...")
        yt = YouTube(download_link)
        print(f"Youtube title: {yt.title}")
        yt.streams.filter(file_extension=file_extension).order_by(
            "resolution").desc().first().download(filename=filename)
        print("Download finish!")


def read(path):
    frames = []
    cap = cv2.VideoCapture(path)
    ret = True
    while ret:
        ret, img = cap.read()  # img is (H, W, C)
        if ret:
            frames.append(img)
    video = np.stack(frames, axis=0)  # dimensions (T, H, W)
    return video


def read_gray(path):
    frames = []
    cap = cv2.VideoCapture(path)
    ret = True
    while ret:
        ret, img = cap.read()  # img is (H, W, C)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # gray is (H, W)
        if ret:
            frames.append(gray)
    video = np.stack(frames, axis=0)  # dimensions (T, H, W)
    return video


def play_by_frame(data):
    if type(data) is not np.ndarray:
        raise TypeError(f"Invalid data type from attribute 'data' in "
                        f"function 'play': expect {np.ndarray}, but "
                        f"{type(data)} received")
    for frame in data:
        print(frame.shape)
        cv2.imshow("frame", frame)
        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
