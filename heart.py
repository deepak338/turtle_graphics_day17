import turtle as t

tim = t.Turtle()
t.listen()
tim.speed("fastest")


def curve():
    for i in range(200):
        tim.right(1)
        tim.forward(1)


def heart():
    tim.color("red", "pink")
    tim.begin_fill()
    tim.left(140)
    tim.forward(111.65)
    curve()

    tim.left(120)
    curve()
    tim.forward(111.65)
    tim.end_fill()
    t.done()


heart()

screen = t.Screen()
screen.exitonclick()
