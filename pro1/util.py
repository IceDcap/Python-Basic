#!/usr/bin/env python
# coding=utf-8

# 文本块生成器

# lines生成器只是在文件的最后追加一个空行
def lines(file):
    for line in file:yield line
    yield '\n'

# blocks生成器当生成一个块后，它里面的行会被连接起
# 来形成一个字符串，并且将开始和结尾中的多余的空格
# 删除，得到一个代表块的字符串
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
