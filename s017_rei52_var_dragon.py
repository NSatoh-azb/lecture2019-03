# -*- coding: utf-8 -*-
"""
例52
  ドラゴン曲線の変形版
@author: NSatoh
"""

import math
import turtlesvg as ttl
t = ttl.Turtle()

def var_dragon(n, length, theta, next_scale, sgn):
    if n == 0:
        t.fd(length)
    else:
        # 現在の向きを記憶
        current_angle = t.heading()
        # 現在の位置を記憶
        current_pos = t.pos()
           
        t.lt(theta * sgn)
        var_dragon(n-1, length*next_scale, theta, next_scale, 1)
            
        # 次の位置を計算
        c = math.cos(math.radians(current_angle))
        s = math.sin(math.radians(current_angle))
        next_x = current_pos[0] + length*c
        next_y = current_pos[1] + length*s
        next_angle  = t.towards(next_x, next_y)
        next_length = t.distance(next_x, next_y)
            
        t.setheading(next_angle)
        var_dragon(n-1, next_length, theta, next_scale, -1)

        # 向きを復元
        t.setheading(current_angle)

t.tracer(0)

t.pencolor('white')
t.bgcolor('black')
n = 15 # 20だとわりと時間がかかる
var_dragon(n, 500, 80, 0.37, 1)

t.update()
t.save_as_svg('017_rei52_output.svg')