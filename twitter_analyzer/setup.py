#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Haotian Zhang (AlexHtZhang)

import codecs
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.

      :input: *parts
      :type: str
      :return: f.read()
      :type: str 
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()

setup(
  name = 'vaderSentiment',
  #packages = ['vaderSentiment'], # this must be the same as the name above
  packages = find_packages(exclude=['tests*']), # a better way to do it than the line above -- this way no typo/transpo errors
  include_package_data=True,
  version = '1.0',
  description = 'VADER Sentiment Analysis. VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts from other domains.',
  long_description=read("README.rst"),
  author = 'Haotian Zhang (AlexHtZhang)',
  author_email = 'h2zhang@ucsd.edu',
  license = 'MIT License: http://opensource.org/licenses/MIT',
  url = 'https://git.ucsd.edu/h2zhang/ece180_winter2018_group8/', # use the URL to the github repo
  download_url = 'https://git.ucsd.edu/h2zhang/ece180_winter2018_group8/archive/master.zip', 
  keywords = ['vader', 'sentiment', 'analysis', 'opinion', 'mining', 'nlp', 'text', 'data', 
              'text analysis', 'opinion analysis', 'sentiment analysis', 'text mining', 'twitter sentiment',
              'opinion mining', 'social media', 'twitter', 'social', 'media'], # arbitrary keywords
  classifiers = ['Development Status :: 4 - Beta', 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License', 'Natural Language :: English',
                 'Programming Language :: Python :: 2.7', 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Scientific/Engineering :: Information Analysis', 'Topic :: Text Processing :: Linguistic',
                 'Topic :: Text Processing :: General'],
)