# anytensor
Want to build a tensor example library for researchers.


## Install

Install by running:

```commandline
python setup.py install
```

## Example

```python
import anytensor

data = anytensor.realworld.video.eagle()
print(data.shape)
```

`data`'s type is `numpy.ndarray`.

`video.eagle()`, `video.friends()`, `video.logo()`, `video.
walking_past_camera()`, `video.walking_past_camera_gray()` is supported now.

## Build Document

```commandline
pip install sphinx sphinx-book-theme sphinx-autoapi recommonmark
cd doc
bash build.sh
```

And then open `doc/build/html/index.html` to view document.