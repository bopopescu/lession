'''

# -*- coding: UTF-8 -*-
i = s = 0
# while i <=10:
#     s += i
#     i += 1
#     print(s)

while True:
    s += i
    i += 1
    if i>10:
        break
print(s)
s= 0
for i in range(0,11,2):
    s += i
print(s)

x = input('input two number:')
a,b =map(int,x.split())
if a>b:
    a,b = b,a
print(a,b)
chTest = ['1','2','3','4','5']
if chTest:
    print(chTest)
else:
    print('Enpty')



'''


#
# import time
#
# result = []
# start = time.time()
# for i in range(10000):
#     result = result + [i]
# print(len(result), ',', time.time()-start)
#
# result = []
# start = time.time()
# for i in range(10000):
#     result.append(i)
# print(len(result), ',', time.time()-start)
#
#
#
# #可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc(1,2))
#
#
#
# nums = [1,2,3]
# print(calc(*nums))
#
#
# #关键字参数
#
#
#
#
# def person(name,age,**kw):
#     print('name:',name,'age:',age,'other:',kw)
#
#
# print(person('Michael',30))
# print(person('Bob',35,city='Beijing'))
# print(person('Adam',45,gender='M',job = 'Engineer'))
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=extra['city'], job=extra['job'])
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, **extra)
#
# # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
#
#
#
#
#
# #如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# def person1(name, age, *, city, job):
#     print(name, age, city, job)
#
# person1('Jack', 24, city='Beijing', job='Engineer')
#
#
#
#


import copy

will = ["Will", 28, ["Python", "C#", "JavaScript"]]
wilber = copy.deepcopy(will)

print id(will)
print(will)
print [id(ele) for ele in will]
print id(wilber)
print wilber
print [id(ele) for ele in wilber]

will[0] = "Wilber"
will[2].append("CSS")
print id(will)
print will
print [id(ele) for ele in will]
print id(wilber)
print wilber
print [id(ele) for ele in wilber]


















