#在 Python 中，元组也是多个元素按照一定顺序构成的序列。元组和列表的不同之处在于，元组是不可变类型，
# 这就意味着元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能修改。
# 如果试图修改元组中的元素，将引发TypeError错误，导致程序崩溃。
# 定义元组通常使用形如(x, y, z)的字面量语法，元组类型支持的运算符跟列表是一样的


# 定义一个三元组
t1 = (35, 12, 98)
# 定义一个四元组
t2 = ('骆昊', 43, True, '四川成都')

# 查看变量的类型
print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>

# 查看元组中元素的数量
print(len(t1))  # 3
print(len(t2))  # 4

# 索引运算
print(t1[0])    # 35
print(t1[2])    # 98
print(t2[-1])   # 四川成都

# 切片运算
print(t2[:2])   # ('骆昊', 43)
print(t2[::3])  # ('骆昊', '四川成都')

# 循环遍历元组中的元素
for elem in t1:
    print(elem)

# 成员运算
print(12 in t1)         # True
print(99 in t1)         # False
print('Hao' not in t2)  # True

# 拼接运算
t3 = t1 + t2
print(t3)  # (35, 12, 98, '骆昊', 43, True, '四川成都')

# 比较运算
print(t1 == t3)            # False
print(t1 >= t3)            # False
print(t1 <= (35, 11, 99))  # False