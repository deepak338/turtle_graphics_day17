import turtle as t
import random

tkinker = t.Turtle()
tkinker.shape('triangle')
tkinker.color('gray')

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]


def shape(no_of_sides):
    angle = 360 / no_of_sides
    for y in range(no_of_sides):
        tkinker.forward(100)
        tkinker.right(angle)


for i in range(3, 11):
    tkinker.color(random.choice(colors))
    shape(i)

screen = t.Screen()
screen.exitonclick()
