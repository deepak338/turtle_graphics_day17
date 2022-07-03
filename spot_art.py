# import colorgram
import turtle as t
import random


# # Extracting colors using colorgram.py.
# colors = colorgram.extract('image.jpg', 30)
# rgb_color=[]
# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     new_color=(r,g,b)
#     rgb_color.append(new_color)
#
# print(rgb_color)


tim = t.Turtle()
t.colormode(255)
colors_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
               (222, 201, 136)
    , (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
               (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
               (183, 205, 171),
               (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
               (176, 192, 208), (168, 99, 102)]

tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)


def dotted_lines():
    for i in range(10):
        tim.dot(10, random.choice(colors_list))
        tim.penup()
        tim.forward(30)


def next_line():
    tim.left(90)
    tim.forward(30)
    tim.left(90)
    tim.penup()
    tim.forward(300)
    tim.right(180)


def spotted_art():
    for i in range(10):
        dotted_lines()
        next_line()


spotted_art()

screen = t.Screen()
screen.exitonclick()
