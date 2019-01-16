''' 求'''
# for n in range(100, 1, -1):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#         else:
#             print(n)
#             break
''' 求100以内的最大素数'''

for n in range(100, 1, -1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)
        break
# '''求100以内的全部素数'''
# for n in range(100, 1, -1):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n)
# '''求1~100之间能被7整除，但不能同时被5整除的所有整数'''
# for i in range(1, 101):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i)
#
# '''求200以内能被17整除的最大正整数。'''
#
# for i in range(200, 0, -1):
#     if i % 17 == 0:
#         print(i)
#         break
# '''打印九九乘法表'''
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{0}*{1}={2}'.format(i, j, i * j).ljust(6), end=' ')
#     print()
#
# '''判断一个数是否为素数。'''
# impor

#
# n = input('Input an inter:')
# n = int(n)
# m = math.ceil(math.sqrt(n)+1)
# for i in range(2, m):
#     if n%i == 0 and i<n:
#         print('No')
#         break
# else:
#     print('Yes')
#
# '''鸡兔同笼问题。假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只。'''
#
# for ji in range(0, 31):
#     if 2*ji + (30-ji)*4 == 90:
#         print('ji:', ji, ' tu:', 30-ji)
# '''编写程序，计算百钱买百鸡问题。假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？'''
#
# #假设能买x只公鸡，x最大为20
# for x in range(21):
#     #假设能买y只母鸡，y最大为33
#     for y in range(34):
#         #假设能买z只小鸡
#         z = 100-x-y
#         if (z%3==0 and 5*x + 3*y + z//3 == 100):
#               print(x,y,z)
#
#





#
