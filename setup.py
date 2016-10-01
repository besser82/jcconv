# -*- coding: utf-8 -*-
# Copyright (c) 2009-2012, Matsumoto Taichi <taichino@gmail.com>
# Copyright (c) 2015,      Juan Moreno <morenosan@gmail.com>
# Copyright (c) 2015,      Alex Willmer <alex@moreati.org.uk>
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import with_statement

from setuptools import setup
import codecs
import os

with codecs.open(os.path.join('README.rst'), encoding='utf-8') as f:
    long_description = f.read().strip()


setup(
    packages         = ['jcconv'],
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
