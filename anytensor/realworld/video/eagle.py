"""
Piotr Indyk et al. “Learning-Based Low-Rank Approximations” Neural Information Processing Systems (2019).
http://youtu.be/ufnf_q_3Ofg
"""

import os.path

import anytensor.core.video as video
from anytensor.core.config import temp_path
from anytensor.core.dataset import Dataset


def __eagle():
    download_link = "http://youtu.be/ufnf_q_3Ofg"
    filename = os.path.join(temp_path, "eagle.mp4")
    video.download_youtube(download_link, filename, "mp4")
    data = video.read(filename)
    return data


eagle = Dataset("eagle", "realworld/video", __eagle)
