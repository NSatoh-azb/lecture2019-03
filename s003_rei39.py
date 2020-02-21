# -*- coding: utf-8 -*-
"""
例39：
  正n角形を m重に描く．
@author: NSatoh
"""

import turtlesvg as ttl
import math

t = ttl.Turtle()

t.speed(0)
t.tracer(0)
t.ht()

def polygon(n, e=200, m=15):
    if m > 0:
        # 1辺の長さeの正n角形を描く
        for i in range(n):
            t.fd(e)
            t.rt(360/n)

        t.penup()
        t.fd(e/2)

        # 次の辺の長さは余弦定理で求めた
        c = math.cos(math.radians(360/n))
        next_e = e * (2 + 2*c)**0.5 /2
        t.rt(360/n/2)
        t.pendown()

        polygon(n, next_e, m-1)
    else:
        t.update()

#-----------------------------------
        
polygon(5)
t.save_as_svg('003_rei39_output.svg')