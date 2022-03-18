'''
O. A. Malik and S. Becker. Low-Rank Tucker Decomposition of Large Tensors Using TensorSketch. Advances in Neural Information Processing Systems 32, pages 10096-10106, 2018.
https://figshare.com/articles/media/Walking_Past_Camera/15135186?file=29084181
https://figshare.com/ndownloader/files/29084181
'''
import os.path

import anytensor.realworld.video.video as video
from anytensor.core.config import temp_path
from anytensor.core.dataset import Dataset


def __walking_past_camera():
    download_link = "https://figshare.com/ndownloader/files/29084181"
    filename = os.path.join(temp_path, "walking_past_camera.mp4")
    video.download(download_link, filename)
    data = video.read(filename)
    return data


walking_past_camera = Dataset("walking_past_camera", "realworld/video",
                              __walking_past_camera)


def __walking_past_camera_gray():
    download_link = "https://figshare.com/ndownloader/files/29084181"
    filename = os.path.join(temp_path, "walking_past_camera.mp4")
    video.download(download_link, filename)
    data = video.read_gray(filename)
    return data


walking_past_camera_gray = Dataset("walking_past_camera_gray",
                                   "realworld/video",
                                   __walking_past_camera_gray)
