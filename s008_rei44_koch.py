# -*- coding: utf-8 -*-
"""
例44
  コッホ曲線とコッホ雪片．
@author: NSatoh
"""

import turtlesvg as ttl
t = ttl.Turtle()

def koch(length, n):
    if n == 0:
        t.forward(length)
    else:
        koch(length/3, n-1)
        t.left(60)
        koch(length/3, n-1)
        t.right(120)
        koch(length/3, n-1)
        t.left(60) 
        koch(length/3, n-1)



# 以下は次の問39(1)用
'''
t.tracer(0)

for i in range(3):
    koch(300, 3)
    t.right(120) # ここを「t.left(120)」にするとどうなるか？

t.update()

t.save_as_svg('008_rei44_output.svg')
'''
