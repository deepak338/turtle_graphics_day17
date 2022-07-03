import turtle as t
import random

tim = t.Turtle()
tim.color('grey')
tim.shape('arrow')
tim.pensize(10)
t.colormode(255)

dir=[0,90,180,270]

def ran_col_gen():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    col_gen=(r,g,b)
    return col_gen

for i in  range(50):
    tim.color(ran_col_gen())
    tim.forward(40)
    tim.right(random.choice(dir))
