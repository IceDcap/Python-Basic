# 6.魔法方法、属性和迭代器
利用双下划线包裹一个属性或者一个方法就成为了一个魔法方法例如__init__,语句__metaclass__=type放在模块的最开始可以确保类是新型的。
## 6.1 构造方法
构造方法是一个魔法方法，在Python中创建一个构造方法很容易，只要使用__init__即可
```Python
class FooBar:
    def __init__(self):
        self.somevar = 42
>>> f=FooBar()
>>> f.somevar
42
```

### 6.1.1 重写一般方法和特殊的构造方法
重写方法一般发生在子类中，重写一般的方法很简单，同理构造方法的重写也一样
```Python
>>> class Bird:
...     def __init__(self):
...             self.hungry = True
...     def eat(self):
...             if self.hungry:
...                     print 'Aaaah...'
...                     self.hungry = False
...             else:
...                     print 'No, thanks!'
... 
>>> b=Bird()
>>> b.eat()
Aaaah...
>>> b.eat()
No, thanks!
>>> class SongBird(Bird):
...     def __init__(self):
...             self.sound = 'Squawk!'
...     def sing(self):
...             print self.sound
... 
>>> sb = SongBird()
>>> sb.sing()
Squawk!
```
由于SongBird是Bird的一个子类，它继承了eat方法，但如果调用eat方法就会出现问题
```Python
>>> sb.eat()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
File "<stdin>", line 5, in eat
AttributeError: SongBird instance has no attribute 'hungry'
```
异常清楚的说明SongBird没有hungry特性因为SongBird构造方法重写了但并没有初始化hungry所以会报此错误
为了达到预期效果必须在子类的构造方法中必须调用超类Bird的构造方法来确保hungry的初始化工作，具体操作可以分为两种：调用超类构造方法的未绑定版本，或者使用super函数

### 6.1.2 调用未绑定的超类构造方法

```Python
>>> class SongBird(Bird):
...     def __init__(self):
...             Bird.__init__(self)
...             self.sound = 'Squawk!'
...     def sing(self):
...             print self.sound
... 
>>> sb = SongBird()
>>> sb.sing()
Squawk!
>>> sb.eat()
Aaaah...
>>> sb.eat()
No, thanks!
```

### 6.1.3 使用super函数
    
    __metaclass__ = type # super函数只在新式类中起作用
    class Bird:
        def __init__(self):
            self.hungry = True
            def eat(self):
                if self.hungry:
                    print 'Aaaah...'
                    self.hungry = False
                else:
                    print 'No, thanks!'
                                        
    class SongBird(Bird):
                    
        def __init__(self):
            super(SongBird, self).__init__()
            self.sound = 'Squawk!'
                    
        def sing(self):
            print self.sound

    
    >>> sb = SongBird()
    >>> sb.sing()
    Squawk!
    >>> sb.eat()
    Aaaah...
    >>> sb.eat()
    No, thanks!

## 6.2 成员访问
### 6.2.1 基本的序列和映射规则

1、__len__(self)返回集合中所含项目的数量

2、__getitem__(self, key)返回与所给键对应的值

3、__setitem__(self,key,value)按一定的方式存储和可以相关的value

4、__delitem__(self,key)在对一部分对象使用del语句时候被调用，同时必须删除和元素相关的键

## 6.3 属性
```Python
>>> class Rectangle:
...     def __init__(self):
...             self.width = 0
...             self.height = 0
...     def setSize(self, size):
...             self.width, self.height = size
...     def getSize(self):
...             return self.width, self.height
... 
>>> r=Rectangle()
>>> r.width=10
>>> r.height=5
>>> r.getSize()
(10, 5)
>>> r.setSize((150,100))
>>> r.width
150
>>> r.getSize()
(150, 100)
```
### 6.3.1 property函数
```Python
>>> __metaclass__ = type
>>> class Rectangle:
...     def __init__(self):
...             self.width = 0
...             self.height = 0
...     def setSize(self, size):
...             self.width, self.height = size
...     def getSize(self):
...             return self.width, self.height
...     size = property(getSize, setSize)
... 
>>> r = Rectangle()
>>> r.width = 10
>>> r.height = 5
>>> r.size
(10, 5)
>>> r.size = 150, 100
>>> r.width
150
>>> r.size
(150, 100)
```
在这个新版的Rectangle中，property函数创建了一个属性，其中访问器函数被用作参数（先是取值然后是赋值）这个属性命为size，这样一来就不用担心是怎么实现的了可以用同样的方式访问width、height和size

### 6.3.2 静态方法和成员方法
两种方式
```Python
__metaclass__ = type
class Myclass:
    def smeth():
        print 'This is a static method'
    smeth = staticmethod(smeth)

    def cmeth(cls):
        print 'This is a method of ', cls
    cmeth = classmethod(cmeth)

>>> Myclass.smeth()
This is a static method
>>> Myclass.cmeth()
This is a method of  <class '__main__.Myclass'>
```

```Python
__metaclass__ = type
class Myclass:
    @staticmethod
    def smeth():
        print 'This is a static method'

    @classmethod
    def cmeth(cls):
        print 'This is a method of ', cls

>>> Myclass.smeth()
This is a static method
>>> Myclass.cmeth()
This is a method of  <class '__main__.Myclass'>
```

## 6.4 迭代器
迭代的意思是重复的做一些事很多次，就像在循环中做的那样
### 6.4.1 从迭代器中得到序列
```Python
>>> class TestIterator:
...     value = 0
...     def next(self):
...             self.value += 1
...             if self.value > 10: raise StopIteration
...             return self.value
...     def __iter__(self):
...             return self
... 
>>> ti = TestIterator()
>>> list(ti)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## 6.5 生成器
生成器是一种用普通的函数语法定义的迭代器

### 6.5.1 生成器的创建
任何包含yield语句的函数称为生成器
    def flatten(nested):
        for sublist in nested:
            for element in sublist:
                yield element



### 6.5.2 递归生成器
    def flatten(nested):
        try:
            # 不要迭代类似字符串对象
            try: nested + ''
            except TypeError: pass
            else: raise TypeError
            for sublist in nested:
                for element in flatten(sublist):
                    yield element
    except TypeError:
            yield nested

### 6.5.3 通用生成器
生成器是一个包含yield关键字的函数。当它被调用时，在函数体中的代码不会被执行，而会返回一个迭代器。每次请求一个值，就会执行生成器中的代码，直到遇到一个yield或者return语句。yield语句意味着应该生成一个值。return意味着生成器要停止执行。换句话说生成器由两部分组成：生成器的函数和生成器的迭代器。生成器的函数是用def语句定义的，包含yield的部分，生成器迭代器是这个函数的返回部分




