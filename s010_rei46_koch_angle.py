# -*- coding: utf-8 -*-
"""
例46
  角度変更版コッホ
@author: NSatoh
"""

import math
import turtlesvg as ttl
t = ttl.Turtle()


def koch_angle(n, length, theta):
    if n == 0:
        t.fd(length)
    else:
        l1 = length/3
        l2 = l1 / (2*math.cos(math.radians(theta)))
        
        koch_angle(n-1, l1, theta)
        t.left(theta)
        koch_angle(n-1, l2, theta)
        t.right(2*theta)
        koch_angle(n-1, l2, theta)
        t.left(theta)
        koch_angle(n-1, l1, theta)


t.tracer(0)

koch_angle(4, 300, 70)
#koch_angle(4, 300, 40)
#koch_angle(4, 300, -50)

t.update()
t.save_as_svg('010_rei46_output.svg')