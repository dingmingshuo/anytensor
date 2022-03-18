'''
Piotr Indyk et al. “Learning-Based Low-Rank Approximations” Neural Information Processing Systems (2019).
http://youtu.be/L5HQoFIaT4I
'''

from anytensor.realworld.video.video import VideoDataset


class Logo(VideoDataset):
    download_link = "http://youtu.be/L5HQoFIaT4I"
    name = "logo"
    filetype = "mp4"

    def __init__(self, filename=None):
        super().__init__(self.name, self.download_link, self.filetype, filename)
