# anytensor
Want to build a tensor example library for researchers.
Enjoy your commit using [gitmoji](https://gitmoji.dev/)!

## Install

Install by running:

```commandline
>> python setup.py install
```

To use data from NetCDF, you need run the following script first:

Mac OS:
```commandline
>> brew install hdf5 netcdf4
```

For Apple silicon
```commandline
>> brew install hdf5 netcdf4
>> brew list hdf5
/opt/homebrew/Cellar/hdf5/1.12.1/bin/gif2h5
...
>> export HDF5_DIR=/opt/homebrew/Cellar/hdf5/1.12.1/
```

Linux:
```commandline
sudo apt-get install libhdf5-serial-dev netcdf-bin libnetcdf-dev
```

## Example

```python
import anytensor

eagle = anytensor.realworld.video.Logo()
data = eagle.first(50)
print(data.shape)
```

`data`'s type is `numpy.ndarray`.

`realworld.video.Eagle()`, `realworld.video.Friends()`, `realworld.video.Logo()` is supported now.

## Build Document

```commandline
>> pip install sphinx sphinx-book-theme sphinx-autoapi recommonmark
>> cd doc
>> bash build.sh
```

And then open `doc/build/html/index.html` to view document.