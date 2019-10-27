# Theme searcher

Simple search engine with async web server as api.
Use GET to <http://localhost:8000/search?text=search_text> to get theme.
Theme is determined by hardcoded corpus (see web.py). Also one can use Searcher class to instantiate
custom search engine.

## How to run

from dir with source

```shell
python -m theme_searcher
```

or if you want to install it:

```shell
pip install .
python -m theme_searcher
```

## How to test

```shell
python3 -m unittest tests
```

or

```shell
python3 setup.py test
```

## Usefull links

- <https://webdevblog.ru/podhody-lemmatizacii-s-primerami-v-python/>
