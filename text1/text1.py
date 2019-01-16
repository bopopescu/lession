# coding:utf-8
"""
import turtle
#彩色螺线线
turtle.pensize(2)
turtle.bgcolor("black")
colors = ['red', 'yellow', 'purple', 'blue']
turtle.tracer(False)
for x in range(400):
    turtle.forward(2 * x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)
turtle.done()

"""

import turtle as t


#   定义一个曲线绘制函数

def DegreeCurve(n, r, d=1):
    for i in range(n):
        t.left(d)
        t.circle(r, abs(d))


# 初始位置设定
s = 0.2  # size
t.setup(450 * 5 * s, 750 * 5 * s)
t.pencolor('black')
t.fillcolor('red')
t.speed(100)
t.penup()
t.goto(0, 900 * s)
t.pendown()

# 绘制花朵形状
t.begin_fill()
t.circle(200 * s, 30)
DegreeCurve(60, 50 * s)
t.circle(200 * s, 30)
DegreeCurve(4, 100 * s)
t.circle(200 * s, 50)
DegreeCurve(50, 50 * s)
t.circle(350 * s, 65)
DegreeCurve(40, 70 * s)
t.circle(150 * s, 50)
DegreeCurve(20, 50 * s, -1)
t.circle(400 * s, 60)
DegreeCurve(18, 50 * s)
t.fd(250 * s)
t.right(150)
t.circle(-500 * s, 12)
t.left(140)
t.circle(550 * s, 100)
t.left(27)
t.circle(650 * s, 100)
t.left(130)
t.circle(-300 * s, 20)
t.right(123)
t.circle(220 * s, 57)
t.end_fill()

# 绘制花枝形状

t.left(120)
t.fd(280 * s)
t.left(115)
t.circle(300 * s, 33)
t.left(180)
t.circle(-300 * s, 33)
DegreeCurve(70, 255 * s, -1)
t.circle(350 * s, 104)
t.left(90)
t.circle(200 * s, 105)
t.circle(-500 * s, 63)
t.penup()
t.goto(170 * s, -30 * s)
t.pendown()
t.left(160)
DegreeCurve(20, 2500 * s)
DegreeCurve(220, 250 * s, -1)
# 绘制一个绿色叶子
t.fillcolor('green')
t.penup()
t.goto(670 * s, -180 * s)
t.pendown()
t.right(140)
t.begin_fill()
t.circle(300 * s, 120)
t.left(60)
t.circle(300 * s, 120)
t.end_fill()
t.penup()
t.goto(180 * s, -550 * s)
t.pendown()
t.right(85)
t.circle(600 * s, 40)
t.circle(600 * s, 40)

# 绘制另一个绿色叶子
t.penup()
t.goto(-150 * s, -1000 * s)
t.pendown()
t.begin_fill()
t.rt(120)
t.circle(300 * s, 115)
t.left(75)
t.circle(300 * s, 100)
t.end_fill()
t.penup()
t.goto(430 * s, -1070 * s)
t.pendown()
t.right(30)
t.circle(-600 * s, 35)
t.done()

import  keyword
print(keyword.kwlist)
print(dir(__builtins__))


m =12.57432
print('|%f|' % m)
print('|%8.1f|' % m)
print('|%8.2f|'%m)
print('|%-8.1f|'%m)
print('|%-8.0f|'%m)




# -*- coding: UTF-8 -*-
#根据三角形边长求三角形面积
# Filename : test.py
# author by : www.runoob.com
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))

# 计算半周长
s = (a + b + c) / 2

# 计算面积
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为 %0.2f' % area)




# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.runoob.com

# 用户输入摄氏温度

# 接收用户输入
celsius = float(input('输入摄氏温度: '))

# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahrenheit))














