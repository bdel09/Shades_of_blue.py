#Name: Benjamin Del Barrio
#Email: benjamin.delbarrio31@myhunter.cuny.edu

import turtle
tess = turtle.Turtle()
tess.shape()
tess.backwards(100)

for i in range(0,255,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(0,i//2,i/255)
