from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.ref()
        score.INCRESE_SCORE()
        snake.extend()

    # collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # collision with the tail
    for segments in snake.seg:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments)< 10:
            is_game_on=False
            score.game_over()

screen.exitonclick()
