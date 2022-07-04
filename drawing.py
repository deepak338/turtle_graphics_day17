import turtle as t

tim = t.Turtle()
screen = t.Screen()


def turn_right():
    tim.right(30)


def turn_left():
    tim.left(30)


def forward():
    tim.forward(10)


def backward():
    tim.back(10)


screen.listen()
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)

screen.exitonclick()
