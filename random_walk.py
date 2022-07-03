import turtle as t
import random as r

tim = t.Turtle()
tim.color('grey')
tim.shape('arrow')
tim.pensize(10)

dir=[0,90,180,270]
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]

for i in  range(50):
    tim.color(r.choice(colors))
    tim.forward(60)
    tim.right(r.choice(dir))
