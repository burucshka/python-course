from turtle import *
from math import cos,radians
setup(640,640)
bgcolor('white')
color('red')
R = 300 #Logo Radius
r = R*cos(radians(30))*2/3
for i in range(3):
    begin_fill()
    fd(r)
    rt(60)
    fd(r)
    lt(60)
    bk(r)
    rt(60)
    bk(r)
    rt(60)
    end_fill()
hideturtle()
done()