# -*- encoding=utf8 -*-
"""First, we should import the module:

        >>> from pinyin import hanzi2pinyin

Remember, the input text should be in unicode format, and the output is unicode too.

We test pure Chinese text:

        >>> hanzi2pinyin('公共的模'.decode('utf8'))
        u'gonggongdemo'

If it is a English string, it keep the same:

        >>> hanzi2pinyin(u'This is an English sentence')
        u'This is an English sentence'

Mixtured text works too:

        >>> hanzi2pinyin('公共的  模 abc'.decode('utf8'))
        u'gonggongde  mo abc'
"""

if __name__ == '__main__':
   import doctest
   doctest.testmod()
