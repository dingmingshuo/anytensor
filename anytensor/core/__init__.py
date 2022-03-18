import os

from . import config
from . import dataset

if not os.path.exists(config.temp_path):
    os.mkdir(config.temp_path)
