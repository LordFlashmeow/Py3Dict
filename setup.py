from setuptools import setup

setup(name='pydictionay2',
      version='1.0',
      description='A python module to get meanings, synonyms and antonyms',
      url='http://github.com/LordFlashmeow/PyDictionary2',
      author='LordFlashmeow',
      author_email='dash098@gmail.com',
      license='MIT',
      packages=['pydictionay2'],
      install_requires=[
          'requests',
          'BeautifulSoup4'
      ]
      zip_safe=False)
