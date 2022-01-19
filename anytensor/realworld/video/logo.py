'''
Piotr Indyk et al. “Learning-Based Low-Rank Approximations” Neural Information Processing Systems (2019).
http://youtu.be/L5HQoFIaT4I
'''

import os.path

import anytensor.core.video as video
from anytensor.core.config import temp_path
from anytensor.core.dataset import Dataset


def __logo():
    download_link = "http://youtu.be/L5HQoFIaT4I"
    filename = os.path.join(temp_path, "logo.mp4")
    video.download_youtube(download_link, filename, "mp4")
    data = video.read(filename)
    return data


logo = Dataset("logo", "realworld/video", __logo)
