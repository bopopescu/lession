

#!/usr/bin/python3

#a = 10
#b = 20



'''
f (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")


'''


import math
import random


#and or not

#优先级，（）> not > and > or
#x or y x为非零，则返回x
#ps int ---> bool 飞凌转换成bool True 0 转换成bool 是False

print(2>1 and 1<4)
print(2>1 and 1>4 or 2>3 and 9>6 or 2< 4 and 3<2)


print(1 or 2)
print(3 or 2)
print(0 or 2)
print(0 or 100)
print(bool(2))
print(bool(0))
#bool --->int
print(int(True))   # 1
print(int(False))  # 0

'x and y x True,则返回'
print(1 and 2)


print([1,2,3]+[4,5,6])
print((1,2,3)+(4,))
print('abcd'+'1234')
print(True+3)
print(False+3)
print(3)
print("a"*10)
print([1,2,3]*3)
print((1,2,3)*3)
print(3in[1,2,3])
print(5 in range(1,10))
for i in range(1,10):
    print(i)
print('abc'in 'abcdef')
print('ac'in 'abcdef')
for i in (3,5,7):
    print(i,end='\t')
print(3 is 3)
x=[300,300,300]
print(x[0]is x[1])

x = [1,2,3]
y = [1,2,3]
print(x is y)
print(3<<2)
print(3&7)
print(3|8)
print(3^5)
print(math.sin(0.5))
print(random.randint(1,100))
print(dir(math))
print(help(math))
print({1,2,3}|{3,4,5})
print({1,2,3}&{3,4,5})
print({1,2,3}^{3,4,5})
print({1,2,3}-{3,4,5})



# 逻辑运算符and 和 or 具有惰性求值特点
print(3>5 and a>3)#
#print(3>5 or b>3)#3>5的值 是True，不需要计算后面的表达式
print(3<5  or a>3)


print(3 and 5)
print(3 and 5>2)
print(3 not in [1,2,3])
print(3 is not 5)
print('a'in 'b','a')
print('a' in ('b','a'))







