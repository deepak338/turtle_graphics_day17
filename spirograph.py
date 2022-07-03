import turtle as t
import random

tim = t.Turtle()
tim.color('black')
t.colormode(255)


def ran_col_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    col_gen = (r, g, b)
    return col_gen


tim.speed('fastest')


def spirograph(size_gen):
    for i in range(int(360 / size_gen)):
        tim.color(ran_col_gen())
        tim.circle(100)
        tim.setheading(tim.heading() + size_gen)


spirograph(5)

screen = t.Screen()
screen.exitonclick()
