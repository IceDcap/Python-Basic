#!/usr/bin/env python
# coding=utf-8

# 打印一些开始标记
# 打印每个段落标签括起来的块
# 打印一些结束标记

import sys, re
from util import *
print '<html><head><title>初次迭代</title><body>'

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'

print '</body></html>'
