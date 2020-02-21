# -*- coding: utf-8 -*-
"""
例49
  コッホ雪片のグラデーション01
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


def multiple_koch_color1(n=5, length=400, theta_max=60, theta_step=1):
    t.pu()

    colors = ["#ff0000", "#ff7700", "#ffff00", "#77ff00", "#00ff00", 
              "#007700", "#007777", "#0077ff", "#0000ff", "#7700ff", 
              "#770077", "#ff0077"]
              
    t.bgcolor('black')
    
    # 外側
    for theta in range(theta_max, 0, -theta_step):
        color = colors[int(abs(theta)/4) % 12]
        t.fillcolor(color)
        t.begin_fill()
        for i in range(3):
            koch_angle(n, length, theta)
            t.right(120)
            
        t.right(60)
        for i in range(3):
            t.fd(length)
            t.left(120)
        t.left(60)
        t.end_fill()

    # 内側
    for theta in range(-theta_max, 1, theta_step):
        color = colors[int(abs(theta)/4) % 12]
        t.fillcolor(color)
        t.begin_fill()
        for i in range(3):
            koch_angle(n, length, theta)
            t.right(120)
            
        t.right(60)
        for i in range(3):
            t.fd(length)
            t.left(120)
        t.left(60)
        t.end_fill()

#-----------------------------------------------------------

t.tracer(0)

multiple_koch_color1()

t.update()
t.save_as_svg('013_rei49_output.svg')

