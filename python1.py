print("hello world")
print('hello world')
print("你好 世界")
print(0x111)
print(11)
a=10
print(a)
print(float(a))
print(a+1*50)
a+=1
print(a)
a+=1
print(a)

f=(input("请输入一个数字"))
q=(float(f)/10)+1
print(q)
print(f)

high=(input("请输入身高"))
weight=(input("请输入体重"))
MBI=(float(weight)/(float(high)*float(high)))
print(MBI)
if MBI<18.5:
    print("过轻")
elif MBI<24:
    print("正常")
else:
    print("过重")
