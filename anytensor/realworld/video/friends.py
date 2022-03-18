'''
Piotr Indyk et al. “Learning-Based Low-Rank Approximations” Neural Information Processing Systems (2019).
http://youtu.be/xmLZsEfXEgE
'''

from anytensor.core.video import VideoDataset


class Friends(VideoDataset):
    download_link = "http://youtu.be/xmLZsEfXEgE"
    name = "friends"
    filetype = "mp4"

    def __init__(self, filename=None):
        super().__init__(self.name, self.download_link, self.filetype, filename)
