import turtle as t
import random as r

is_game_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput('place your bet', 'choose the color of the turtle')
colors = ['red', 'purple', 'blue', 'yellow', 'orange', 'green']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []
for i in range(0, 6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for i in all_turtle:
        if i.xcor() > 230:
            is_game_on = False
            winner = i.pencolor()
            if winner == user_bet:
                print(f"you won , the {winner} turtle win the race")
            else:
                print(f"you lose , the {winner} turtle win the race")

        forward_steps = r.randint(1, 10)
        i.forward(forward_steps)

screen.exitonclick()
