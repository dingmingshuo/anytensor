"""
Piotr Indyk et al. “Learning-Based Low-Rank Approximations” Neural Information Processing Systems (2019).
http://youtu.be/ufnf_q_3Ofg
"""

import os.path

import anytensor.core.video as video
from anytensor.core.config import temp_path
from anytensor.core.dataset import Dataset


class Eagle(Dataset):
    def __download(self):
        download_link = "http://youtu.be/ufnf_q_3Ofg"
        filename = os.path.join(temp_path, "eagle.mp4")
        video.download_youtube(download_link, filename, "mp4")
        data = video.read(filename)
        return data

    def __init__(self):
        super().__init__("eagle", "realworld/video", self.__download)

    def first(self, n):
        download_link = "http://youtu.be/ufnf_q_3Ofg"
        filename = os.path.join(temp_path, "eagle.mp4")
        video.download_youtube(download_link, filename, "mp4")
        data = video.read(filename, n)
        return data
