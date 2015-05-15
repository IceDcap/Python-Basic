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
