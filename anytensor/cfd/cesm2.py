import netCDF4 as nc
from anytensor.core.dataset import Dataset


class CESM2(Dataset):
    def __read(self):
        dataset = nc.Dataset(self.filename)
        masked_data = dataset[self.variable][:]
        data = (~masked_data.mask) * masked_data.data
        return data

    def __init__(self, filename, variable):
        self.name = "CESM2"
        self.filename = filename
        self.variable = variable
        super().__init__(self.name, "cfd", self.__read)
