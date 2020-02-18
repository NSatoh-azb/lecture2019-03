# -*- coding: utf-8 -*-
"""
例38：
　移動距離を増加させながら螺旋状に多角形を描く．
 （a度ずつ右回りに，1回曲がるごとに距離をd増やして移動）
@author: NSatoh
"""

import turtlesvg as ttl
t = ttl.Turtle()

t.speed(0)
t.tracer(0)
#t.ht()

def spiral(a, d=5, n=0, n_max=300):
    if n < n_max:
        t.fd(n)
        t.rt(a)
        spiral(a, d, n+d, n_max)
        t.update()        

# 以下のコメントアウトを外すと，テキストの3つの例が描かれる．
# 自由にパラメータ指定して描かせてみたい場合は，
# このまま実行してからコンソールウィンドウで
# spiral(71, d=1) などを実行せよ．

'''
t.penup()
t.goto(-400, 0)
t.pendown()
spiral(90)

t.penup()
t.goto(0, 0)
t.pendown()
spiral(72)

t.penup()
t.goto(470, 0)
t.pendown()
spiral(71, d=1)

t.penup()
t.save_as_svg('002_rei38.svg')
'''
