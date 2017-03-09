PyDict: A Dictionary Module for Python
======================================

PyDict is an updated and streamlined dictionary module for Python 3 to
get meanings, synonyms, antonyms, and translations. It uses `WordNet`_
for definitions, `Thesaurus.com`_ for synonyms and antonyms, and `Google
Translate`_ for translations.

This module uses ``requests`` and ``BeautifulSoup4`` as dependencies.

Installation
------------

``pip install PyDictionary``

Usage
-----

PyDict is designed with simplicity in mind, which makes it easy to use.

PyDict has only three functions: ``define``, ``synonym`` ,and
``antonym``

Define:
~~~~~~~

.. code:: python

    >>> print(PyDict.define('hello'))
    {'Noun': ['an expression of greeting']}

Synonym:
~~~~~~~~

.. code:: python

    >>> print(PyDict.synonym('happy'))
    ['cheerful', 'contented', 'overjoyed', 'ecstatic', 'elated']

Antonym:
~~~~~~~~

.. code:: python

    >>> print(PyDict.antonym('happy'))
    ['melancholy', 'upset', 'disappointed', 'sorrowful', 'unfriendly']

.. _WordNet: https://wordnet.princeton.edu/
.. _Thesaurus.com: http://www.thesaurus.com/
.. _Google Translate: https://translate.google.com/
