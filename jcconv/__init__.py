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

u"""
   jcconv, Japanese Characters CONVerter, interconvert hiragana, katakana, half-width kana.
   This module also treat 'half/wide number', 'half/wide alphabet'.

   Since 0.2.0, check_hira, check_kata, check_half functions were added.
   you can check if string consists of characters you specified.
   
   IMPOTANT: In current version, this works only with utf-8 encoding.


   Simple example of usage is followings

       >>> from jcconv import *
       >>> print hira2kata('あいうえお')   # hiragana to katakana
       アイウエオ
       >>> print kata2hira('カタカナ')     # katakana to hiragana
       かたかな
       >>> print half2hira('ﾊﾝｶｸｶﾀｶﾅ')      # half-width kana to hiragana
       はんかくかたかな       
       >>> print half2wide('hello jcconv') # half-width alphabet to wide-width
       ｈｅｌｌｏ ｊｃｃｏｎｖ
       >>> print wide2half('ＷＩＤＥ')     # wide-width alphabet to half-width
       wide
"""

from pkg_resources import get_distribution

__author__  = "Matsumoto Taichi"
__version__ = get_distribution('jcconv').version
__license__ = "MIT License"

from .jcconv import *
