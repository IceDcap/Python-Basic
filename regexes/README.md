# 正则表达式
Python中re模块包含对正则表达式的支持

## 什么是正则表达式
正则表达式是可以匹配文本片段的模式。最简单的正则表达式就是普通的字符串，可以匹配其自身，例如'python'可以匹配字符串'python'
* 通配符
例如 .可以匹配任意字符，'.ython'可以匹配'python'或者'jyphon'或者'+ython'但不能匹配'jjython'
* 对特殊字符进行转义
对于'python.org'字符串的匹配当然可以使用其本身'python.org'，但这样的话也可以匹配诸如'pythonzorg'，这样需要转义'python\\.org'才能自会匹配'python.org'
* 字符集
例如 '[pj]ython'能匹配'python'和'jython'，'[a-z]','[a-zA-Z0-9]'也可以通过^符号进行反转'[^abc]'除abc之外的其他任意字符
* 选择符和子模式
在字符串的每个字符都不相同的情况下，字符集是很好用的，但如果只想匹配'python'和'perl'就需要选择符了'python|perl'或者子模式'p(ython|erl)'
* 可选项和重复子模式
在子模式后面加上问号就变成了可选项

'(http://)?(www\\.)?python\\.org'只会匹配

'http://www.python.org'
'http://python.org'
'www.python.org'
'python.org'
除了可选项还有重复子模式
(pattern)*允许模式重复0次或者多次
(pattern)+允许模式重复1次或者多次
(pattern){m,n}允许模式重复m~n次
* 字符串的开始和结尾
字符串开头用^符号匹配结尾用$符号匹配，例如 '^ht+p'会匹配'http://python.org'也会匹配'htttttp://python.org'但不会匹配'www.python.org'

## re模块
一些重要的函数

函数 | 描述
-----|-----
compile(pattern[, flags]) | 根据包含正则表达式的字符串创建模式对象
search(pattern, string[, flags]) | 在字符串中寻找模式
match(pattern, string[, flags]) | 在字符串开始处匹配模式
split(pattern, string[, maxsplit=0]) | 根据模式匹配项来分割字符串
findall(pattern, string) | 列出字符串中模式的所有匹配项
sub(pat, repl, string[, count=0]) | 将字符串中所有的pat的匹配项与repl替换
escape(string) | 将字符串中所有特殊正则表达式字符转义

```Python
>>> import re
>>> if re.search('^w+', 'www.baidu.com'):
...     print 'Found it'
... 
Found it
>>> if re.search('^w+', 'http://www.baidu.com'):
...     print 'Found it'
... 
>>> some_text = 'alpha, beta,,,,,,gamma delta'
>>> re.split('[,]', some_text)
['alpha', ' beta', '', '', '', '', '', 'gamma delta']
>>> re.split('[, ]', some_text)
['alpha', '', 'beta', '', '', '', '', '', 'gamma', 'delta']
>>> some_text = 'alpha, beta, , , , , ,gamma delta'
>>> re.split('[, ]', some_text)
['alpha', '', 'beta', '', '', '', '', '', '', '', '', '', '', 'gamma', 'delta']
>>> some_text = 'alpha, beta,,,,,,gamma delta'
>>> re.split('[, ]', some_text)
['alpha', '', 'beta', '', '', '', '', '', 'gamma', 'delta']
>>> re.split('[, ]', some_text, maxsplit=2)
['alpha', '', 'beta,,,,,,gamma delta']
>>> re.split('[, ]', some_text, maxsplit=1)
['alpha', ' beta,,,,,,gamma delta']
>>> re.split('[, ]', some_text, maxsplit=3)
['alpha', '', 'beta', ',,,,,gamma delta']
>>> some_text = 'alpha,beta,,,,,,gamma delta'
>>> re.split('[, ]', some_text, maxsplit=2)
['alpha', 'beta', ',,,,,gamma delta']
>>> pat = '[a-zA-Z]+'
>>> text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
>>> re.findall(pat, text)
['Hm', 'Err', 'are', 'you', 'sure', 'he', 'said', 'sounding', 'insecure']
>>> pat = r'[.?\-",]+'          # 匹配标点符号，前端加了一个字母r是使用了原始字符串这样可以为转义字符只添加一个反斜杠即可
>>> re.findall(pat, text)
['"', '...', '--', '?"', ',', '.']
>>> pat = '{name}'                                                                                              
>>> text = 'Dear {name}...'
>>> re.sub(pat, 'Mr. Gumby', text)
'Dear Mr. Gumby...'
>>> re.escape('www.python.org')
'www\\.python\\.org'
>>> re.escape('But where is the ambiguity')
'But\\ where\\ is\\ the\\ ambiguity'
```

## 匹配对象和组
对于re模块中的能够对字符串进行模式匹配的函数而言，当能找到匹配项的时候，它们都会返回MatchObject对象。

'There (was a (wee) (cooper)) who (lived in Fyfe)'
包含下面的这些组

0 There was a wee cooper who lived in Fyfe
1 was a wee cooper
2 wee
3 cooper
4 lived in Fyfe

模式 诸如r'www\.(.+)\.com$'

方法 | 描述
-----|-----
group([group1, ...]) | 获取给定子模式（组）的匹配项
start([group]) | 返回给定组的匹配项的开始位置
end([group]) | 返回给定组的匹配项的结束位置（和分片一样，不包括组的结束位置）
span([group]) | 返回一个组的开始和结束位置

```Python
>>> m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
>>> m.group(1)
'python'
>>> m.start(1)
4
>>> m.end(1)
10
>>> m.span(1)
(4, 10)
```

## 作为替换的组号和函数

```Python
>>> emphasis_pattern = re.compile(r'\*([^\*]+)\*')
>>> re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!')
'Hello, <em>world</em>!'
```

## 模板
模板是一种通过放入具体值从而得到某种以完成文本的文件，例如邮件模板，系统模板。。。

简单的例如
'The sum of 7 and 9 is [7+9].'希望得到的结果是'The sum of 7 and 9 is 16.'

方法：
* 使用正则表达式匹配字段，提取内容
* 使用eval计算字符串值，提供包含作用域的字典。可以在try/except语句内进行这项工作，如果引发了SyntaxError异常，可能是某些语句出现了问题（比如赋值），应该使用exec来代替
* 可以使用exec执行字符串（和其他语句）的赋值操作，在字典中保存模板的作用域。
* 使用re.sub将求值的结果替换为处理后的字符串


























