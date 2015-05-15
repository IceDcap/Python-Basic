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
