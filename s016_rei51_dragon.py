# -*- coding: utf-8 -*-
"""
例51
  ドラゴン曲線
@author: NSatoh
"""

import turtlesvg as ttl
t = ttl.Turtle()

def dragon(n, length, sgn):
    if n == 0:
        t.fd(length)
    else:
        if sgn > 0:
            t.lt(45)
            dragon(n-1, length/(2**0.5), 1)
            t.rt(90)
            dragon(n-1, length/(2**0.5), -1)
            t.lt(45)
        else:
            t.rt(45)
            dragon(n-1, length/(2**0.5), 1)
            t.lt(90)
            dragon(n-1, length/(2**0.5), -1)
            t.rt(45)


t.speed(10)
t.tracer(0)

t.penup()
t.goto(-200,0)
t.pendown()

n = 10    
dragon(n,500,1)
t.update()

t.save_as_svg('016_rei51_output.svg')