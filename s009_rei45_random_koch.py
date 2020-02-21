# -*- coding: utf-8 -*-
"""
例45
  ランダムコッホ曲線
  35％の確率でsgn（符号）に-1が代入されるので，回転方向が全て逆になる．
  （つまり35％の確率でトゲを右向きに生成する）
@author: NSatoh
"""
import random
import turtlesvg as ttl
t = ttl.Turtle()

def random_koch(length, n):
    if n == 0:
        t.forward(length)
    else:
        if random.random() <= 0.35:
            sgn = -1 # 符号(signature)
        else:
            sgn = 1
        random_koch(length/3, n-1)
        t.left(60 * sgn)
        random_koch(length/3, n-1)
        t.right(120 * sgn)
        random_koch(length/3, n-1)
        t.left(60 * sgn) 
        random_koch(length/3, n-1)


#-------------------------------------------------
t.tracer(0)
random_koch(300, 4)
t.update()

t.save_as_svg('009_rei45_output.svg')

