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
