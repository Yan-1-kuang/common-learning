#列表操作
list1 = [1, 2, 3, 4, 5]
print(list1)
lange=['Chinese','Math','English','Chinese']
lange.append('French')
print(lange)
a=list1 + lange
print(a)
print(list1 + lange)
print(a*3)
print(1 in list1)
print('Chinese' in lange)
print(list1[0]*9)
list1.insert(1, 100)
print(list1)