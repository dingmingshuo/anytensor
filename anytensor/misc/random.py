import math

import numpy as np

from anytensor.core.dataset import Dataset


class Randomu(Dataset):
    """ Generate a uniformly randomized tensor.
    """

    def __init__(self):
        super().__init__("randomu", None)

    def __call__(self, shape, l=0, r=1):
        return self.getdata(shape, l, r)

    def getdata(self, shape, l=0, r=1):
        if l > r:
            raise AttributeError("'l' should not be larger than 'r'.")
        data = np.random.random(shape) * (r - l) + l
        super().__init__("randomu", data)
        return data


class Randomn(Dataset):
    """ Generate a Gaussian randomized tensor.
    """

    def __init__(self):
        super().__init__("randomn", None)

    def __call__(self, shape, mu=0, sigma2=1):
        return self.getdata(shape, mu, sigma2)

    def getdata(self, shape, mu=0, sigma2=1):
        if sigma2 <= 0:
            raise AttributeError("'sigma2' should larger than zero.")
        data = np.random.randn(*shape) * math.sqrt(sigma2) + mu
        super().__init__("randomn", data)
        return data
