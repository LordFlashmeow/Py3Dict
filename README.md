# PyLexicon: A Dictionary Module for Python

PyLexicon is an updated and streamlined dictionary module for Python 3 to get meanings, synonyms, and antonyms,. It uses [WordNet](https://wordnet.princeton.edu/) for definitions, and [Thesaurus.com](http://www.thesaurus.com/) for synonyms and antonyms.

This module uses `requests` and `BeautifulSoup4` as dependencies.

## Installation

`pip install PyLexicon`

## Usage

PyLexicon is designed with simplicity in mind, which makes it easy to use.

PyLexicon has three functions: `define`, `synonym`, and  `antonym`.

### Importing:

```python
>>> import PyLexicon
```

### Define:

```python
>>> print(PyLexicon.define('hello'))
{'Noun': ['an expression of greeting']}
```

### Synonym:

```python
>>> print(PyLexicon.synonym('happy'))
['cheerful', 'contented', 'overjoyed', 'ecstatic', 'elated']
```

### Antonym:

```python
>>> print(PyLexicon.antonym('happy'))
['melancholy', 'upset', 'disappointed', 'sorrowful', 'unfriendly']
```