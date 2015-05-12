Python-Basic
==============
This repository used for starting python learning.

# 0.前言
Python是一门解释型、面向对象的、带有动态语义的高级程序语言。它有许多发行版本，例如ActivePython、StacklessPython，这两个版本都是标准的Python实现由c语言编写。除此还有Jython和TronPython等等这些是由其他语言实现。

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

# 2.列表和元组
Python中最基本的数据结构是序列（sequence），序列中的每个元素被分配一个序号，即元素的位置，也称为索引，第一个索引是0，之后以此类推。

```Python
>>> x = ['Edward Gumby', 42, True, 'hello', ['hello', 4, 'world']]
>>> x
['Edward Gumby', 42, True, 'hello', ['hello', 4, 'world']]
```
## 2.1序列的操作
序列操作包括：索引（indexing）、分片（slicing）、加（adding）、乘（multiplying）、检查某元素是否属于序列成员以及Python内建函数例如append、count、extend等等

### 2.1.1索引

```Python
>>> greeting = 'Hello'
>>> greeting[2]
'l'
>>> greeting[-1]
'o'
>>> x[4]
['hello', 4, 'world']
```
### 2.1.2分片

```Python
>>> tag = '<a href="http://www.python.org">Python web site</a>'
>>> tag[9:30]
'http://www.python.org'
```
基本样式[下限:上限:步长]

```Python
>>>print s1[:5]             # 从开始到下标4 （下标5的元素 不包括在内）
>>>print s1[2:]             # 从下标2到最后
>>>print s1[0:5:2]          # 从下标0到下标4 (下标5不包括在内)，每隔2取一个元素 （下标为0，2，4的元素）
>>>print s1[2:0:-1]         # 从下标2到下标1

>>> number = [1,2,3,4,5,6,7,8,9,10]
>>> number[-3]
8
>>> number[-3:-1]
[8, 9]
>>> number[-3:0] #这个结果可以这样解释：只要分片中最左端的索引比右边的晚出现在序列中就将返回一个空序列
[]

#步长演示
>>> number[2:9:3]
[3, 6, 9]
>>> number[2:9:2]
[3, 5, 7, 9]
>>> number[2:9:1]
[3, 4, 5, 6, 7, 8, 9]
```

### 2.1.3序列相加

```Python
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> 'Hello ' + 'World'
'Hello World'
>>> [1, 2, 3] + 'world'
Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      TypeError: can only concatenate list (not "str") to list
```

上述错误得知序列相加操作必须建立在元素类型相同的基础上。

### 2.1.4 乘法

```Python
>>> 'python' * 5
'pythonpythonpythonpythonpython'
>>> [42] * 10
[42, 42, 42, 42, 42, 42, 42, 42, 42, 42]
```
None(Python内建值)、空列表([])、初始化
初始化一个长度为10的列表：
```Python
>>> sequence = [None] * 10
>>> sequence
[None, None, None, None, None, None, None, None, None, None]
```

### 2.1.5 成员资格
使用in运算符，返回布尔值若该成员在序列中则为True否则False
```Python
>>> permission = 'rw'
>>> 'w' in permission
True
```

### 2.1.6 长度、最小值、最大值
使用内建函数len、min、max
```python
>>> numbers = [100, 34, 678]
>>> len(numbers)
3
>>> max(numbers)
678
>>> min(numbers)
34
```

## 2.2 列表
列表不同于元组和字符串的地方：列表是可变的，并且列表有许多有用的、专门的方法。

### 2.2.1 list函数
```Python
>>> list('Hello')
['H', 'e', 'l', 'l', 'o']
```
### 2.2.2 列表操作
赋值、删除元素、分片赋值
```Python
>>> x = list('hello')
>>> x
['h', 'e', 'l', 'l', 'o']
>>> x[0] = 'br'
>>> x
['br', 'e', 'l', 'l', 'o']
>>> del x[2]
>>> x
['br', 'e', 'l', 'o']
>>> x[1:] = '3'
>>> x
['br', '3']
>>> x[0:] = list('hello')
>>> x
['h', 'e', 'l', 'l', 'o']
>>> x[1:3] = [1,2,3]
>>> x
['h', 1, 2, 3, 'l', 'o']
```

### 2.2.3 列表方法
1.append
```Python
>>> x = [1,2,3]
>>> x.append([4,5,6])
>>> x
[1, 2, 3, [4, 5, 6]]
>>> x.append('hello')
>>> x
[1, 2, 3, [4, 5, 6], 'hello']
```
2.count
```Python
>>> y = ['ee', 'a', 'be', 'c', 'be']
>>> y.count('be')
2
```

3.extend
```Python
>>> x.extend(y)
>>> x
[1, 2, 3, [4, 5, 6], 'hello', 'ee', 'a', 'be', 'c', 'be']
```

4.index
```Python
>>> x
[1, 2, 3, [4, 5, 6], 'hello', 'ee', 'a', 'be', 'c', 'be']
>>> x.index('ee')
5
```

5.insert
```Python
>>> x.insert(5, 'world')
>>> x
[1, 2, 3, [4, 5, 6], 'hello', 'world', 'ee', 'a', 'be', 'c', 'be']
```

6.pop
```Python
>>> x
[1, 2, 3, [4, 5, 6], 'hello', 'world', 'ee', 'a', 'be', 'c', 'be']
>>> x.pop()
'be'
>>> x
[1, 2, 3, [4, 5, 6], 'hello', 'world', 'ee', 'a', 'be', 'c']
>>> x.pop(0)
1
>>> x
[2, 3, [4, 5, 6], 'hello', 'world', 'ee', 'a', 'be', 'c']
>>> x.pop(2)
[4, 5, 6]
>>> x
[2, 3, 'hello', 'world', 'ee', 'a', 'be', 'c']
```

7.remove
```Python
>>> x
[2, 3, 'hello', 'world', 'ee', 'a', 'be', 'c']
>>> x.remove(2)
>>> x
[3, 'hello', 'world', 'ee', 'a', 'be', 'c']
>>> x.remove('22')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: list.remove(x): x not in list
>>> x.remove('ee')
>>> x
[3, 'hello', 'world', 'a', 'be', 'c']
```

8.reverse
```Python
>>> x
[3, 'hello', 'world', 'a', 'be', 'c']
>>> x.reverse()
>>> x
['c', 'be', 'a', 'world', 'hello', 3]
```

9.sort
```Python
>>> x.sort()
>>> x
[3, 'a', 'be', 'c', 'hello', 'world']
```

10.高级排序


## 2.3 元组：不可变序列
元初始化语法：
```Python
>>> 1,2,3
(1, 2, 3)
>>> (1,2,3)
(1, 2, 3)
>>> 
>>> ()
()

#实现一个值的元组，第一个例子不是元组必须加逗号，即使是一个值
>>> 42
42
>>> 42,
(42,)
>>> (42,)
(42,)
```
(42)和42是完全一样的不属于元组
```Python
>>> 3*(42 + 2)
132
>>> 3*(42+2,)
(44, 44, 44)
```

### 2.3.1 tuple函数
tuple与list函数基本相同，将一个序列转换成元组，如果参数本身就是元组，将直接返回参数。
```Python
>>> tuple([1,2,3])
(1, 2, 3)
>>> tuple('hello')
('h', 'e', 'l', 'l', 'o')
>>> tuple((1,2,3))
(1, 2, 3)
```
### 2.3.2 元组的基本操作
由于元组是不可变序列基本操作也就是创建和访问
```Python
>>> x=1,2,3
>>> x
(1, 2, 3)
>>> x[1]
2
>>> x[0:2]
(1, 2)
```

# 3 字符串

## 3.1 字符串介绍
### 3.1.1 单引号和转义
```Python
>>> "Hello world"
'Hello world'
>>> 'Hello world'
'Hello world'
>>> "Let's go!"                 #对于字符串中含有单引号(或双引号)的情况可以使用双引号(或单引号)包裹或者使用转义
"Let's go!"
>>> 'Let's go !'
  File "<stdin>", line 1
      'Let's go !'
           ^
SyntaxError: invalid syntax
>>> 'Let\'s go !'               #使用转义
"Let's go !"
```

### 3.1.2 拼接字符串
```Python
>>> "Let's say " '"hello"'      #用一个接着另一个的方式写了两个字符串，Python就会自动拼接它们
'Let\'s say "hello"'
>>> x = 'hello'
>>> y = 'world'
>>> x y
  File "<stdin>", line 1
      x y
        ^
SyntaxError: invalid syntax
>>> x + y                       #正确拼接字符串的方法是像加法运算一样
'helloworld'
```

### 3.1.3 字符串的表示，str和repr
上述的几个例子里是直接变量赋值为带引号（单引号或者双引号）的句子，实际是Python将值自动转换为字符串。其实可以通过函数来使用。

```Python
>>> print repr("hello world")
'hello world'
>>> repr('hello')
"'hello'"
>>> print repr(10000L)          #repr(x)也可以写作`x`实现（`是反引号）
10000L
>>> print str("Hello world")
Hello world
>>> str("Hello")
'Hello'
>>> str('Hello')
'Hello'
>>> print str(1000L)
1000
>>> str(1000L)
'1000'
>>> repr(1000L)
'1000L'
```
简而言之，str、repr和反引号是将Python值转换为字符串的3中方法

### 3.1.4 input和raw_input
```Python
>>> name = input('What\'s your name? ')
What's your name? dou
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1, in <module>
NameError: name 'dou' is not defined
>>> name = input('What\'s your name? ')
What's your name? 'dou'
>>> print "Hello, " + name
Hello, dou
```
上述代码可以看出input函数会假设用户输入的是合法的Python表达式，如果以字符串作为输入的名字时程序就能通过。那么解决办法就是使用raw_input()函数了
```Python
>>> name = raw_input('What\'s your name? ')
What's your name? zhao
>>> print name
zhao
```

## 3.2 字符串使用
所有的标准序列操作（索引、分片、乘法、判断成员资格、求长度、取最小值、最大值）对字符串同样适用
### 3.2.1 字符串格式化
```Python
>>> format = "Hello, %s. %s enough for ya?"
>>> values = ('world', 'Hot')
>>> print format % values
Hello, world. Hot enough for ya?
```
代码实例中string_format.py展示了完整版的字符串格式化操作

### 3.2.2 字符串方法
1、find方法可以在一个较长的字符串中查找到子串，它返回子串所在位置最左端索引，如果没有则返回-1
```Python
>>> 'With a moo-moo here, and a moo-moo there'.find('moo')
7
>>> 'With a moo-moo here, and a moo-moo there'.find('bee')
-1
>>> 'With a moo-moo here, and a moo-moo there'.find('with')
-1
>>> 'With a moo-moo here, and a moo-moo there'.find('With')
0
```
2、join方法是字符串非常重要的方法，它是split方法的逆方法，用来连接序列中的元素
```Python
>>> seq = ['1', '2', '3', '4', '5']
>>> seq.join('+')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'join'
>>> sep = '+'
>>> '+'.join(seq)
'1+2+3+4+5'
>>> sep.join(seq)
'1+2+3+4+5'
```
3、lower方法返回字符串的小写字母版
```Python
>>> 'HeLLo'.lower()
    'hello'
```

4、replace方法返回某字符串的所匹配项均被替换之后得到字符串
```Python
>>> 'This is a test'.replace('is', 'azz')
'Thazz azz a test'
```

5、split是一个非常重要的方法，它是join的逆方法，用来将字符串分割成序列。
```Python
>>> '/usr/bi/env'.split('/')
['', 'usr', 'bi', 'env']
>>> ['', 'usr', 'bi', 'env'].join('/')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'join'
>>> '/'.join(['', 'usr', 'bi', 'env'])
'/usr/bi/env'
```

6、strip方法返回去除两侧（不包括内部）空格的字符串
```Python
>>> '         internal whitespace is kept       '.strip()
'internal whitespace is kept'
```

7、translate方法和replace方法一样，可以替换字符串的某些部分，但是和replace不同的是translate方法只处理单个字符，它的优势在于可以同时进行多个替换，有些时候比replace效率高的多。

# 4.字典
数据结构之映射（mapping），字典是Python中唯一内建的映射类型。字典中的值并没有特殊的顺序，但是都存储在一个特定的键（key）下。键可以使数字、字符串甚至是元组。

## 4.1 字典的使用

代码中dict_demo.py是利用字典搭建的小型数据库，字典使用人名作为key，每个人用另一个字典表示，其键'phone'和'addr'分别表示他们的电话号码和地址。

## 4.2 创建和使用字典

### 4.2.1 dict函数
类似于list,tuple(列表，元组)函数，dict是是生成字典函数。
```Python
>>> items = [('name', 'Gumby'), ('age', '42')]
>>> dict(items)
{'age': '42', 'name': 'Gumby'}
>>> d = dict(items)
    >>> d
{'age': '42', 'name': 'Gumby'}
>>> d['name']
'Gumby'
>>> d = dict(name = 'Dou', age = 25)
>>> d
{'age': 25, 'name': 'Dou'}
```

### 4.2.2 字典的基本操作
字典的基本操作很多方面与序列类似
* len(d)返回d中项（键值对）的数量
* d[k]返回关联到键k上的值
* d[k]=v将值v关联到键k上
* del d[k]删除键位k的项
* k in d检查d中是否有含有键为k的项
字典与列表的区别
* 键类型：字典的键不一定为整型数据，键可以使任意不可变的类型，比如浮点型（实型）、字符串或者元组
* 自动添加：即使键起初在字典中并不存在，也可以为它赋值，这样字典就会建立新的项，对于序列如果不使用append方法或者其他类似操作的情况下不能将值关联到列表范围以外的索引上。
* 成员资格：k in d（d为字典）查找的是键，而不是值。表达式v in l（l为列表）使用来查找值，而不是索引

### 4.2.3 字典格式化字符串
```Python
>>> phonebook = {'Beth':'9102', 'Alice':'2304', 'Cecil': '7882'}
>>> "Cecil's phone number is %(Cecil)s." % phonebook                # %(k)s用以匹配字典中键所对应的值
"Cecil's phone number is 7882."
```

### 4.2.4 字典方法
1、clear方法清除字典中所有的项，这是个原地操作（类似于list.sort）,所以无返回值（或者说返回None）。
```Python
>>> d = {}
>>> d ['name'] = 'Gumby'
>>> d ['age'] = '42'
>>> d
{'age': '42', 'name': 'Gumby'}
>>> v = d.clear()
>>> v
>>> print v
None
>>> d
{}
```

2、copy方法返回一个具有相同键值对的新字典（这种方法实现的是浅复制shallow copy，因为值本身就是相同的，而不是副本）
```Python
>>> x = {'username':'dou', 'machines':['foo', 'bar', 'baz']}
>>> y = x.copy()
    >>> y
{'username': 'dou', 'machines': ['foo', 'bar', 'baz']}
>>> y['machines'].remove('bar')
>>> y
{'username': 'dou', 'machines': ['foo', 'baz']}
>>> x
{'username': 'dou', 'machines': ['foo', 'baz']}
>>> y['username'] = 'hello'
>>> y
{'username': 'hello', 'machines': ['foo', 'baz']}
>>> x
{'username': 'dou', 'machines': ['foo', 'baz']}
```
在副本中替换值的时候原始字典不受影响，但是如果修改了某个值的话原始字典也会被修改，解决办法使用深复制deepcopy

```Python
>>> from copy import deepcopy
>>> d = {}
>>> d['name'] = ['Alfred', 'Bertrand']
>>> c = d.copy()
>>> dc = d.deepcopy()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'deepcopy'
>>> dc = deepcopy(d)
>>> d['name'].append('Clive')
>>> c
{'name': ['Alfred', 'Bertrand', 'Clive']}
>>> dc
{'name': ['Alfred', 'Bertrand']}
```

3、fromkeys方法使用给定的键建立新的字典，每个键都对应一个默认的值None
```Python
>>> {}.fromkeys(['name', 'age'])
{'age': None, 'name': None}
>>> {}.fromkeys(['name', 'age'],'unknow')               #提供默认的值unknown
{'age': 'unknow', 'name': 'unknow'}
```

4、get方法是一个宽松的访问字典项的方法
```Python
>>> d = {}
>>> print d['name']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'name'
>>> print d.get('name')
None
```

5、has_key方法可以检查字典中的是否含有特定的键。表达式d.has_key(k)相当于表达式k in d
```Python
>>> d = {}
>>> d.has_key('name')
False
>>> d['name'] = 'dou'
>>> d.has_key('name')
True
```

6、items和iteritems将字典中的项以列表形式返回，iteritems方法大致相同，但是会返回一个迭代器对象而不是列表
```Python
>>> d = {'title':'Python', 'url':'www.python.org'}
>>> d.items()
[('url', 'www.python.org'), ('title', 'Python')]
>>> it = d.iteritems()
>>> it
<dictionary-itemiterator object at 0x106f74470>
>>> list(it)
[('url', 'www.python.org'), ('title', 'Python')]
```

7、keys和iterkeys将字典中的键以列表形式返回，而iterkeys则返回针对键的迭代器。

8、values和itervalues以列表的方式返回字典中的值，itervalues返回迭代器，与返回键的列表不同的是返回值的列表中可以包含重复的元素
```Python
>>> d={}
>>> d[1]=1
>>> d[2]=2
>>> d[3]=3
>>> d[4]=4
>>> d.values()
[1, 2, 3, 4]
```

9、pop方法用来返回对应给定键的值，然而将这个键值对从字典中移除。
```Python
>>> d = {'x':1, 'y':2}
>>> d.pop('x')
1
>>> d
{'y': 2}
```

10、popitem类似于list.pop，后者弹出列表中的最后一个元素，但不同的是，popitem弹出随机项，因为字典没有顺序的概念

11、setdefault方法在某种程度上类似于get方法，除此之外该方法可以为字典中不含有给定键的情况下设定相应的键值
```Python
>>> d = {}
>>> d.setdefault('name', 'N/A')
'N/A'
>>> d
{'name': 'N/A'}
>>> d['name'] = 'Gumby'
>>> d.setdefault('name', 'N/A')
'Gumby'
>>> d
{'name': 'Gumby'}
```

12、update利用一个字典项更新另一个字典
```Python
>>> d = {'title':'Python Web Site','url':'http://www.python.org','changed':'Mar 14 22:09:15 MET 2008'}
>>> x = {'title':'Python Language Website'}
>>> d.update(x)
>>> d
{'url': 'http://www.python.org', 'changed': 'Mar 14 22:09:15 MET 2008', 'title': 'Python Language Website'}
```









