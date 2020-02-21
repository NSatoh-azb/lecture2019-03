# -*- coding: utf-8 -*-
"""
問37：
  一筆版シェルピンスキ・ガスケット．
@author: NSatoh
"""

import turtlesvg as ttl
t = ttl.Turtle()

t.speed(10)

def var_sierpinski(length, n):
    if n > 0:
        for i in range(3):
            t.fd(length)
            t.left(120)
            var_sierpinski(length * 0.5, n-1)

#----------------------------------------------------
# var_sierpinski(100, 5)
