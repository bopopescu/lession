import math

'''


'''
s = input('请输入一个数 ')  # 这是一个输入语句
s = float(s)
if s > 0:
    s = math.sqrt(s)
    print(s)
else:
    print('没有平方根')

# !/usr/bin/python3

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c)

a = 10
b = 5
c = a // b
print("7 - c 的值为：", c)




