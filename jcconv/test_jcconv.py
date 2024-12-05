# -*- coding: utf-8 -*-

import unittest
from jcconv import *

class JcconvTest(unittest.TestCase):
    def testKana(self):
        # hira => kata, half
        text1 = 'あいうえおがぎぐげごぱぴぷぺぽ'
        self.assertEqual(hira2kata(text1), 'アイウエオガギグゲゴパピプペポ')
        self.assertEqual(hira2half(text1), 'ｱｲｳｴｵｶﾞｷﾞｸﾞｹﾞｺﾞﾊﾟﾋﾟﾌﾟﾍﾟﾎﾟ')
        text2 = 'にほんごしょりはめんどくさい'
        self.assertEqual(hira2kata(text2), 'ニホンゴショリハメンドクサイ')
        self.assertEqual(hira2half(text2), 'ﾆﾎﾝｺﾞｼｮﾘﾊﾒﾝﾄﾞｸｻｲ')

        # kata => hira, half
        text1 = 'ナゼカサンシュルイモモジガアル'
        self.assertEqual(kata2hira(text1), 'なぜかさんしゅるいももじがある')
        self.assertEqual(kata2half(text1), 'ﾅｾﾞｶｻﾝｼｭﾙｲﾓﾓｼﾞｶﾞｱﾙ')

        # half => hira, kata
        text1 = 'ｿｺﾃﾞｿｳｺﾞﾍﾝｶﾝｷﾉｳｶﾞﾋﾂﾖｳﾆﾅﾙ'
        self.assertEqual(half2hira(text1), 'そこでそうごへんかんきのうがひつようになる')
        self.assertEqual(half2kata(text1), 'ソコデソウゴヘンカンキノウガヒツヨウニナル')

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
