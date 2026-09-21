x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'{y = }') #大括号里面变量名后面写个等号，自动打印「变量名 = 值」
print(y )