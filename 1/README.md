# 1.基本的语法知识
## 1.1 变量
变量基本上就是代表（或者引用）某值的名字
```Python
>>> x = 3   #变量赋值
>>> x
3
>>> x * 2
6
```
变量名可以包括字母、数字和下划线，变量不能以数字开头。

## 1.2 获取用户输入
input()函数
```Python
>>> x = input('x: ')
x: 5
>>> y = input('y: ')
y: 6
>>> x * y
30
```

## 1.3 函数
例如：pow(),abs()等等

## 1.4 模块
可以把模块想象成导入到Python以增强其功能的扩展。使用import关键字进行导入模块
```Python
>>> import math
>>> math.floor(32.9)
32.0
>>> from math import sqrt
>>> sqrt(9)
3.0
```
