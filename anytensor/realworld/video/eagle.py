"""
Piotr Indyk et al. “Learning-Based Low-Rank Approximations” Neural Information Processing Systems (2019).
http://youtu.be/ufnf_q_3Ofg
"""

from anytensor.realworld.video.video import VideoDataset


class Eagle(VideoDataset):
    download_link = "http://youtu.be/ufnf_q_3Ofg"
    name = "eagle"
    filetype = "mp4"

    def __init__(self, filename=None):
        super().__init__(self.name, self.download_link, self.filetype, filename)
