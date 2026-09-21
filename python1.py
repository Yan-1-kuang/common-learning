s1 = 'hello, world!'
s2 = "你好，世界！"
s3 = '''hello,
wonderful
world!'''
print(s1)
print(s2)
print(s3)
s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
#\t、\r和\n都是转义字符。\t是制表符（table），\n是换行符（new line），
# \r是回车符（carriage return）相当于让输出回到了行首。
# Python 中有一种以r或R开头的字符串，这种字符串被称为原始字符串，意思是字符串中的每个字符都是它本来的含义，
# 没有所谓的转义字符。
print(s1)
print(s2)

print(ord('a')) 

s = 'hello, world!'
print(s.find('or'))      # 8
print(s.find('or', 9))   # -1
print(s.find('of'))      # -1
print(s.index('or'))     # 8
print(s.index('or', 9)) 
#find方法找不到指定的字符串会返回-1，index方法找不到指定的字符串会引发ValueError错误。