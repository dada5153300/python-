# 俩个数字使用的
from decimal import *
from fractions import Fraction

# 内置对象
# python内的变量常量都是指针 因此数字不会像java那样有限制，超过了就变奇怪了

# 数字 他是没有大小限制的
# 1.Python3.6.x开始支持在数字中间位置使用单个下划线作为分隔来提高数字的可读性，
# 类似于数学上使用逗号作为千位分隔符
# 2.标准库fractions的Fraction对象支持分数
# from fractions import Fraction
fen_shu1 = Fraction(3, 5)
print(fen_shu1)
print(fen_shu1.numerator)    # 分子
print(fen_shu1.denominator)  # 分母
num_big = 100_000
print(type(num_big))
num1 = 1     # int
num2 = 1.1   # float
num3 = 1+1j  # 复数
# 解决浮点数精度问题
a = Decimal('4.2')
b = Decimal('2.1')
c = a * b
print(c)
# 字符串 str 以字目R或r引导来表示原生字符串
# 1.字符串界定符前面加字母r或R表示原始字符串，
# 其中的特殊字符不进行转义，但字符串的最后一个字符不能是\。
# 原始字符串主要用于正则表达式、文件路径或者URL的场合
# 2.字符串是用单引号、双引号或三引号界定的符号系列
# 单引号、双引号、三单引号、三双引号可以互相嵌套，
# 用来表示复杂字符串'abc'、'123'、'中国'、"Python"、'''Tomsaid,"Let'sgo"'''
# 字符串属于不可变序列
# 3.空字符串表示为''或""
# 4.三引号'''或"""表示的字符串可以换行
str1 = "demo3_1"
str2 = 'b'
str3 = "'c'"
str4 = R"假的换行\n"
str5 = "真的换行\n"
print(str5)
print(str4)

# 字节串 bytes 仅限于ASCII字符，中文表示不了
bytes1 = b"a44a4"
bytes1 = b"'a44a4'"
bytes1 = b'a44a4'
print(bytes1)
# bytes2 = b'高达'
# print(bytes2)

# 列表 里面的元素的类型随意，可以是字典可以试试list可以是str也可以是自己定义的
list1 =[1, 2, 3]

# 字典 dict 键对值 键唯一 值能重复
dict1 = {1: "demo3_1", 2: "demo3_1", 3: "b"}
print(dict1)

# 集合 set frozenset
# 元素不允许重复;另外，set是可变的，而frozenset是不可变的
set1 = {1, 2, 3}
set2 = set({1, 2, 3})
frozenset1 = frozenset({1, 2, 3})
print(type(set1))
print(type(set2))
print(type(frozenset1))
# 布尔型 True False
# 元组 特殊:元素不可变 tuple
tuple1 = (2, 3, 4)
tuple3 = 100, 000
print(type(tuple3))
print(tuple1)
# 只有一个元素时，必须带,如果不带他会被定义成int类型
# tuple2 = (3)
tuple2 = (3,)
print(type(tuple2))

# 空类型
NoneType1 = None
print(type(NoneType1))

# 异常 Exception ValueError TypeError

# 文件
file1 = open("第一次课学习说明", 'rb')
print(file1.read().decode('utf-8'))    # 查看文件内容

# 其他可迭代对象
# range对象 filter对象 map对象 zip对象
# 表达式不在它被绑定到变量之后就立即求值,而是在该值被取用的时候求值 参考 惰性求值 - 维基百科,自由的百科全书

# 编程单元 def 函数定义 class class定义 模块
# 类和函数都属于可调用对象 模块用于集中存放函数、类、常量或其他对象
