# anytensor
Want to build a tensor example library for researchers.
Enjoy your commit using [gitmoji](https://gitmoji.dev/)!

## Install

Install by running:

```commandline
python setup.py install
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
pip install sphinx sphinx-book-theme sphinx-autoapi recommonmark
cd doc
bash build.sh
```

And then open `doc/build/html/index.html` to view document.