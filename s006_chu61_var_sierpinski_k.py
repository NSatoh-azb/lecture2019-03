# -*- coding: utf-8 -*-
"""
注意61
  一筆シェルピンスキ k角形版
@author: NSatoh
"""

import turtlesvg as ttl
t = ttl.Turtle()
t.speed(0)
t.tracer(0)

def var_sierpinski_k(length, k, n, r=0.5):
    if n > 0:
        for i in range(k):
            t.fd(length)
            t.left(360/k)
            var_sierpinski_k(length * r, k, n-1, r)

t.bgcolor('black')
t.pencolor('white')
var_sierpinski_k(100, 7, 4, r=0.5)

t.update()

t.save_as_svg('006_chu61_output.svg')