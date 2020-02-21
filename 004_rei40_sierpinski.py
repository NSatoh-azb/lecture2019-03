# -*- coding: utf-8 -*-
"""
例40
  シェルピンスキのガスケットを描く．
@author: NSatoh
"""

import turtlesvg as ttl
t = ttl.Turtle()

def middle_pt(A, B):
    # ABの中点を返す
    return ( (A[0] + B[0]) / 2, (A[1] + B[1]) / 2 )

def draw_triangle(A, B, C):
    t.penup()
    t.goto(A)
    t.pendown()

    t.goto(B)
    t.goto(C)
    t.goto(A)

def sierpinski(A, B, C, n):
    if n > 0:
        P = middle_pt(A, B)
        Q = middle_pt(B, C)
        R = middle_pt(C, A)
        draw_triangle(P, Q, R)
        
        sierpinski(A, P, R, n-1) 
        sierpinski(B, Q, P, n-1) 
        sierpinski(C, R, Q, n-1) 

#----------------------------------------------------
        
B = (-300, -200)
C = ( 300, -200)
A = (   0, -200 + 300 * 3**0.5)

sierpinski(A, B, C, 5)
draw_triangle(A, B, C)

t.save_as_svg('004_rei40_output.svg')
