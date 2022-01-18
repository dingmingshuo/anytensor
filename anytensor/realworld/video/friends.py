'''
Piotr Indyk et al. “Learning-Based Low-Rank Approximations” Neural Information Processing Systems (2019).
http://youtu.be/xmLZsEfXEgE
'''

import os.path

import anytensor.core.video as video
from anytensor.core.config import temp_path
from anytensor.dataset import Dataset


def __friends():
    download_link = "http://youtu.be/xmLZsEfXEgE"
    filename = os.path.join(temp_path, "friends.mp4")
    video.download_youtube(download_link, filename, "mp4")
    data = video.read(filename)
    return data


friends = Dataset("friends", "realworld/video", __friends)
