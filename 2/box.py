#!/usr/bin/env python
# coding=utf-8
#以正确的宽度在居中的盒子里内打印一句话
sentence = raw_input("Sqntence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
print
print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'
print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
print ' ' * left_margin + '| ' + sentence + ' |'
print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'

