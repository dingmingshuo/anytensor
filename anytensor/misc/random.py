import math

import numpy as np

from anytensor.core.dataset import Dataset


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
"""
Generate a uniformly randomized tensor.
"""


class __randomn(Dataset):
    def __init__(self):
        super().__init__("randomn", None)

    def __call__(self, shape, mu=0, sigma2=1):
        if sigma2 <= 0:
            raise AttributeError("'sigma2' should larger than zero.")
        data = np.random.randn(*shape) * math.sqrt(sigma2) + mu
        super().__init__("randomn", data)
        return data


randomn = __randomn()
"""
Generate a Gaussian randomized tensor.
"""

