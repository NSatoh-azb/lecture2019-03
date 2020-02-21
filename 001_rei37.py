# -*- coding: utf-8 -*-
"""
例37：
　正三角形を描きながら円周上を動く．
@author: NSatoh
"""

import turtlesvg as ttl
t = ttl.Turtle()

t.speed(10)
# t.tracer(0)

n = 12
for i in range(360//n):
    # 円周上を移動
    t.fd(25)
    t.rt(n)
    # 正三角形を描く
    for j in range(3):
        t.fd(125)
        t.rt(120)

# t.update()

t.penup()
t.save_as_svg('001_rei37_output.svg')