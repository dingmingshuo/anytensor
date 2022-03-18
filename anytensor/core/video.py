import os
from urllib.request import urlopen
from anytensor.core.config import temp_path
from anytensor.core.dataset import Dataset

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


def read(path, frame=None):
    frames = []
    cap = cv2.VideoCapture(path)
    if frame is None:
        ret = True
        while ret:
            ret, img = cap.read()  # img is (H, W, C)
            if ret:
                frames.append(img)
    else:
        for i in range(frame):
            ret, img = cap.read()  # img is (H, W, C)
            if ret:
                frames.append(img)
    video = np.stack(frames, axis=0)  # dimensions (T, H, W)
    return video


def read_gray(path, frame=None):
    frames = []
    cap = cv2.VideoCapture(path)
    if frame is None:
        ret = True
        while ret:
            ret, img = cap.read()  # img is (H, W, C)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # gray is (H, W)
            if ret:
                frames.append(gray)
    else:
        for i in range(frame):
            ret, img = cap.read()  # img is (H, W, C)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # gray is (H, W)
            if ret:
                frames.append(gray)
    video = np.stack(frames, axis=0)  # dimensions (T, H, W)
    return video


def play_by_frame(data, delay=1000):
    if type(data) is not np.ndarray:
        raise TypeError(f"Invalid data type from attribute 'data' in "
                        f"function 'play': expect {np.ndarray}, but "
                        f"{type(data)} received")
    print("Press q to exit")
    for frame in data:
        cv2.imshow("frame", frame)
        cv2.waitKey(delay)


class VideoDataset(Dataset):
    def __download(self):
        file = os.path.join(temp_path, self.filename)
        download_youtube(self.download_link, file, self.filetype)
        data = read(file)
        return data

    def __read(self):
        data = read(self.filename)
        return data

    def __init__(self, name, download_link=None, filetype="mp4", filename=None):
        if filename is None:
            self.download_link = download_link
            self.name = name
            self.filetype = filetype
            self.filename = name + "." + filetype
            super(VideoDataset, self).__init__(self.name, "realworld/video", self.__download)
        else:
            # Already downloaded
            self.filename = filename
            super(VideoDataset, self).__init__(self.name, "realworld/video", self.__read)

    def first(self, n):
        file = os.path.join(temp_path, self.filename)
        download_youtube(self.download_link, file, self.filetype)
        data = read(file, n)
        return data
