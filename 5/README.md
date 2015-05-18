# 5.面向对象和异常处理

## 5.1 面向对象概念略

1、类定义
```Python
>>> class Bird(object):
...     have_feather = True
...     way_of_reproduction = 'egg'
... 
>>> summer = Bird()
>>> print summer.way_of_reproduction
egg


__metaclass__ = type    # 确定新式类

class Person:
       
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello, world! I'm %s." % self.name

foo = Person()
foo.setName('Monkey D Luffy')
foo.greet()

```

2、动作(方法,函数)
```Python
>>> class Bird:
...     song = 'twitter!'
...     def sing(self):
...             print self.song
... 
>>> bird = Bird()
>>> bird.sing()
twitter!
```

3、私有方法和特性（在名字前加双下划线）
```Python
>>> class Secretive:
...     def __inaccessible(self):
...             print "Bet you can't see me"
...     def accessible(self):
...             print "The secret message is: "
...             self.__inaccessible()
... 
>>> s = Secretive()
>>> s.__inaccessible()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Secretive' object has no attribute '__inaccessible'
>>> s.accessible()
The secret message is: 
Bet you can't see me
```

4、类命名空间（局部、全局）
```Python
>>> class MemberCounter:
...     members = 0
...     def init(self):
...             MemberCounter.members += 1
... 
>>> m1 = MemberCounter()
>>> m1.init()
>>> MemberCounter.members
1
>>> m2 = MemberCounter()
>>> MemberCounter.members
1
>>> m2.init()
>>> MemberCounter.members
2
>>> m1.members
2
>>> m2.members
2
```

5、超类
```Python
>>> class Filter:
...     def init(self):
...             self.blocked = []
...     def filter(self, sequence):
...             return [x for x in sequence if x not in self.blocked]
... 
>>> class SPAMFilter(Filter):           # SPAMFilter是Filter的子类
...     def init(self):                 # 重写init方法
...             self.blocked = ['SPAM']
... 
>>> f = Filter()
>>> f.init()
>>> f.filter([1,2,3])
[1, 2, 3]
>>> s = SPAMFilter()
>>> s.init()
>>> s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'egg', 'bacon', 'SPAM'])
['egg', 'bacon']
```

6、检查继承

使用内建函数issubclass
```Python
>>> issubclass(SPAMFilter, Filter)
True
>>> issubclass(Filter, SPAMFilter)
False
```

如果想要知道该类的基类可以使用该类的特殊性__base__
```Python
>>> SPAMFilter.__base__
<class '__main__.Filter'>
>>> Filter.__base__
<type 'object'>
```

如果只想知道一个类属于哪个类，可以使用__class__特性
```Python
>>> s.__class__                 # s是SPAMFilter的一个实例
<class '__main__.SPAMFilter'>
>>> f.__class__                 # f是Filter的一个实例
<class '__main__.Filter'>
```

7、多个超类
```Python
>>> class Calcultor:
...     def calculate(self, expression):
...             self.value = eval(expression)
... 
>>> class Talker:
...     def talk(self):
...             print 'Hi, my value is', self.value
... 
>>> class TalkingCalculator(Calcultor, Talker):
...     pass
... 
>>> tc = TalkingCalculator()
>>> tc.calculate('1+2*3')
>>> tc.talk()
Hi, my value is 7
```

## 5.2 异常处理

### 5.2.1 自定义异常
1、raise语句
    
为引发异常可以使用一个类（应该是Exception子类）或者实例参数调用raise语句

```Python
>>> raise Exception
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception
>>> raise Exception('hyperdrive overload')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception: hyperdrive overload
```
第一个例子raise Exception引发一个没有任何信息的普通异常后一个例子中添加了错误信息hyperdrive overload

```Python
# 利用dir函数查看exceptions模块所包含的类
>>> import exceptions
>>> dir(exceptions)
    ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'EnvironmentError', 'Exception', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__doc__', '__name__', '__package__']
```

实际中一些常见的类如下表所示

类名 | 描述
-----|-----
Exception | 所有异常的基类
AttributeError | 特性引发或赋值失败时引发
IOError | 试图打开不存在的文件(包含其他情况)时引发
IndexError | 在使用序列中不存在的索引时引发
KeyError | 在使用映射中不存在键时引发
NameError | 再找不到名字（变量）时引发
SyntaxError | 在代码为错误形式时引发
TypeError | 在内建操作或者函数应用于错误类型的对象时引发
ValueError | 在内键操作或者函数应用于正确类型的对象，但是该对象使用不合适的值时引发
ZeroDivisionError | 在除法或者模除操作的第二个参数为0时引发

2、自定义异常类
尽管内建类已经够用了但是有些时候还是需要自定义异常类。

class SomeCustomException(Exception): pass


### 5.2.2 异常捕获
使用语句try/except语句捕获异常
```Python
>>> try:
...     x = input('Enter the first number: ')
...     y = input('Enter the second number: ')
...     print x / y
... except ZeroDivisionError:
...     print "the second number can't be zero!"
... 
Enter the first number: 3
Enter the second number: 0
the second number can't be zero!
```

### 5.2.3 多异常捕获
```Python
>>> try:
...     x = input('Enter the first number: ')
...     y = input('Enter the second number: ')
...     print x / y
... except ZeroDivisionError:
...     print "the second number can't be zero!"
... except TypeError:
···     print "That wasn't a number, was it?"
```

### 5.2.4 用一个块捕捉两个异常
```Python
>>> try:
...     x = input('Enter the first number: ')
...     y = input('Enter the second number: ')
...     print x / y
... except (ZeroDivisionError, TypeError, NameError):
...     print 'Your numbers were bogus...'
... 
Enter the first number: 3
Enter the second number: s
Your numbers were bogus...
```

### 5.2.5 捕捉对象
如果希望except子句中访问异常对象本身，可以使用两个参数，如果想让程序继续运行又想因为某种原因记录错误，此功能就很有用。
```Python
>>> try:
...     x = input('Enter the first number: ')
...     y = input('Enter the second number: ')
...     print x / y
... except (ZeroDivisionError, TypeError, NameError), e:
...     print e
... 
Enter the first number: e
name 'e' is not defined
>>> try:
...     x = input('Enter the first number: ')
...     y = input('Enter the second number: ')
...     print x / y
... except (ZeroDivisionError, TypeError, NameError), e:
...     print e
... 
Enter the first number: 3
Enter the second number: 0
integer division or modulo by zero
```

### 5.2.6 全捕捉
```Python
>>> try:
...     x = input('Enter the first number: ')
...     y = input('Enter the second number: ')
...     print x / y
... except:
...     print 'Something wrong'
... 
Enter the first number: 3
Enter the second number: 0
Something wrong
```

### 5.2.7 异常与控制语句
```Python
>>> while True:
...     try:
...             x = input('Enter the first number: ')
...             y = input('Enter the second number: ')
...             value = x/y
...             print 'x/y is', value
...     except:
...             print 'Invalid input. Please try again.'
...     else:
...             break
... 
Enter the first number: 1
Enter the second number: 0
Invalid input. Please try again.
Enter the first number: 'foo'
Enter the second number: 'bar'
Invalid input. Please try again.
Enter the first number: baz
Invalid input. Please try again.
Enter the first number: 10
Enter the second number: 5
x/y is 2
```

### 5.2.8 finally语句

finally子句可以用来在可能的异常后进行清理，它和try子句联合使用，一般用于关闭文件或者网络套接字
```Python
>>> x=None
>>> try:
...     x = 1/0
... finally:
...     print 'Cleaning up...'
...     del x
... 
Cleaning up...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> print x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

### 5.2.9 异常和函数
异常和函数能很自然的工作在一起，如果异常在函数内引发而不被处理，它就会传播至函数调用的地方，如果在那里也没有处理异常，它就会继续传播，一直到达主程序，如果那里也没有处理异常，程序会带着栈跟踪中止。
```Python
>>> def faulty():
...     raise Exception('Something is wrong')
... 
>>> def ignore_exception():
...     faulty()
... 
>>> def handle_exception():
...     try:
...             faulty()
...     except:
...             print 'Exception handled'
... 
>>> ignore_exception()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in ignore_exception
  File "<stdin>", line 2, in faulty
Exception: Something is wrong
>>> handle_excaption()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'handle_excaption' is not defined
>>> handle_exception()
Exception handled
```










