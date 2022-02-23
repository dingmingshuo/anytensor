import numpy as np


class Dataset:
    """
    Dataset class.
    """

    def __init__(self, name, category, data=None):
        self.name = name
        self.category = category
        if type(data) is np.ndarray:
            self.data = data
            self.shape = self.data.shape
        elif callable(data):
            self.data = data
            self.data_is_got = False
            self.shape = "Unknown"
        elif data is None:
            self.data = None
            self.shape = "Unknown"
        else:
            raise TypeError(f"Invalid data type of attribute 'data' in "
                            f"class 'Dataset': expect {np.ndarray} or a "
                            f"non-attribute function with a return "
                            f"value of {np.ndarray}, but {type(data)} "
                            f"received.")

    def __str__(self):
        if self.data is not None:
            return f"Dataset name: {self.name}\n\tCategory: " \
                   f"{self.category}\n\tData shape:" \
                   f" {self.shape}"
        else:
            return f"Dataset name: {self.name}\n\tCategory: " \
                   f"{self.category}\n\tData: None " \
                   f"or not be set."

    def __call__(self):
        return self.getdata()

    def getdata(self):
        if callable(self.data) and (not self.data_is_got):
            self.data = self.data()
            if type(self.data) is not np.ndarray:
                raise TypeError(f"Get invalid data type from the callable "
                                f"attribute 'self.data' in class 'Dataset': "
                                f"expect {np.ndarray}, but {type(self.data)} "
                                f"received")
            self.shape = self.data.shape
            self.data_is_got = True
        return self.data

    def first(self, n):
        return self.getdata()[:n]

    def info(self):
        return self.__str__()
