# -*- coding: utf-8 -*-
from __future__ import with_statement

from setuptools import setup
import codecs
import os

with codecs.open(os.path.join('README.rst'), encoding='utf-8') as f:
    long_description = f.read().strip()


if __name__ == '__main__':
  # build distribution package
  setup(
    packages         = ('jcconv',),
    name             = 'jcconv',
    version          = '0.2.3',
    description      = 'jcconv "JapaneseCharacterCONVerter", interconvert hiragana, katakana, halfwidth kana',
    long_description = long_description,
    author           = 'Matsumoto Taichi',
    author_email     = 'taichino@gmail.com',
    url              = 'http://github.com/taichino/jcconv',
    keywords         = 'japanese converter, hiragana, katakana, half-width kana',
    license          = 'MIT License',
    classifiers      = ["Development Status :: 3 - Alpha",
                        "Intended Audience :: Developers",
                        "License :: OSI Approved :: MIT License",
                        "Operating System :: POSIX",
                        "Programming Language :: Python :: 2",
                        "Programming Language :: Python :: 2.5",
                        "Programming Language :: Python :: 2.6",
                        "Programming Language :: Python :: 2.7",
                        "Programming Language :: Python :: 3",
                        "Programming Language :: Python :: 3.3",
                        "Programming Language :: Python :: 3.4",
                        "Programming Language :: Python :: 3.5",
                        "Topic :: Software Development :: Libraries :: Python Modules"],
    include_package_data = True,
    tests_require = ['six'],
    test_suite = "tests",
    install_requires = ['six'],
    )
