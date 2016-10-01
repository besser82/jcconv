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

import unittest
from jcconv.jcconv import *

class JcconvTest(unittest.TestCase):
    def testKana(self):
        # hira => kata, half
        text1 = u'あいうえおがぎぐげごぱぴぷぺぽ'
        self.assertEqual(hira2kata(text1), u'アイウエオガギグゲゴパピプペポ')
        self.assertEqual(hira2half(text1), u'ｱｲｳｴｵｶﾞｷﾞｸﾞｹﾞｺﾞﾊﾟﾋﾟﾌﾟﾍﾟﾎﾟ')
        text2 = 'にほんごしょりはめんどくさい'
        self.assertEqual(hira2kata(text2), 'ニホンゴショリハメンドクサイ')
        self.assertEqual(hira2half(text2), 'ﾆﾎﾝｺﾞｼｮﾘﾊﾒﾝﾄﾞｸｻｲ')

        # kata => hira, half
        text1 = u'ナゼカサンシュルイモモジガアル'
        self.assertEqual(kata2hira(text1), u'なぜかさんしゅるいももじがある')
        self.assertEqual(kata2half(text1), u'ﾅｾﾞｶｻﾝｼｭﾙｲﾓﾓｼﾞｶﾞｱﾙ')

        # half => hira, kata
        text1 = u'ｿｺﾃﾞｿｳｺﾞﾍﾝｶﾝｷﾉｳｶﾞﾋﾂﾖｳﾆﾅﾙ'
        self.assertEqual(half2hira(text1), u'そこでそうごへんかんきのうがひつようになる')
        self.assertEqual(half2kata(text1), u'ソコデソウゴヘンカンキノウガヒツヨウニナル')

    def testWideHalf(self):
        # wide => half
        self.assertEqual(wide2half('Ｍａｃｒｏｓｓ ７'), 'Macross 7')

        # half => wide
        self.assertEqual(half2wide('cherry spitz 1996'), 'ｃｈｅｒｒｙ ｓｐｉｔｚ １９９６')

        # half symbole => wide symbol
        self.assertEqual(half2wide('!%^?'), '！％＾？')

        # wide symbole => half symbol
        self.assertEqual(half2wide('^^);'), '＾＾）；')

    def testReserve(self):
        res = half2wide('abcde', [u'a', u'e'])
        self.assertEqual(res, 'aｂｃｄe')


if __name__ == '__main__':
    unittest.main()
