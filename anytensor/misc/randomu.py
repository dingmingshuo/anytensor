import numpy as np

from anytensor.dataset import Dataset


class __randomu(Dataset):
    def __init__(self):
        super().__init__("randomu", None)

    def __call__(self, shape, l=0, r=1):
        if l > r:
            raise AttributeError("'l' should not be larger than 'r'.")
        data = np.random.random(shape) * (r - l) + l
        super().__init__("randomu", data)
        return data

randomu = __randomu()