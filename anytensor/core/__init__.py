import os

from . import config
from . import dataset
from . import video

if not os.path.exists(config.temp_path):
    os.mkdir(config.temp_path)
