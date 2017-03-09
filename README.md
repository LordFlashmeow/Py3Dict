# PyDict: A Dictionary Module for Python

PyDict is an updated and streamlined dictionary module for Python 3 to get meanings, synonyms, antonyms, and translations. It uses [WordNet](https://wordnet.princeton.edu/) for definitions, [Thesaurus.com](http://www.thesaurus.com/) for synonyms and antonyms, and [Google Translate](https://translate.google.com/) for translations.

This module uses `requests` and `BeautifulSoup4` as dependencies.

## Installation

`pip install PyDictionary`

## Usage

PyDict is designed with simplicity in mind, which makes it easy to use.

PyDict has only three functions: `define`, `synonym` ,and  `antonym`

### Define:

```python
>>> print(PyDict.define('hello'))
{'Noun': ['an expression of greeting']}
```

### Synonym:

```python
>>> print(PyDict.synonym('happy'))
['cheerful', 'contented', 'overjoyed', 'ecstatic', 'elated']
```

### Antonym:

```python
>>> print(PyDict.antonym('happy'))
['melancholy', 'upset', 'disappointed', 'sorrowful', 'unfriendly']
```