# -*- coding: utf-8 -*-

"""
    jcconv, Japanese Characters CONVerter, interconvert hiragana, katakana, half-width kana.
    This module also treats 'half/wide number', 'half/wide alphabet'.

    Since v0.2.0, the check_hira, check_kata, check_half functions were added.
    You can check if a string consists of the characters you specified.

    IMPORTANT: In the current version, this module is tested to work with
               utf-8 encoding, only.

    A simple example of usage is as follows:

        >>> from jcconv import *
        >>> print(hira2kata('あいうえお'))   # hiragana to katakana
        アイウエオ
        >>> print(kata2hira('カタカナ'))     # katakana to hiragana
        かたかな
        >>> print(half2hira('ﾊﾝｶｸｶﾀｶﾅ'))	  # half-width kana to hiragana
        はんかくかたかな
        >>> print half2wide('hello jcconv')) # half-width alphabet to wide-width
        ｈｅｌｌｏ ｊｃｃｏｎｖ
        >>> print(wide2half('ＷＩＤＥ'))     # wide-width alphabet to half-width
        wide
"""

__author__  = "Matsumoto Taichi"
__version__ = "0.2.3"
__license__ = "MIT License"

from jcconv import *
