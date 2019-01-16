# from contextlib import contextmanager
#
# class Query(object):
#
#     def __init__(self,name):
#         self.name = name
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
#
# @contextmanager
# def creat_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')




# def now():
#     print('2015-3-25')
#
# f = now
# f()
#
# print(now.__name__)
# print(f.__name__)
#
#
# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s()' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
#
# @log
# def now():
#     print('2015-3-25')
#
# print(now())


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(1000)
