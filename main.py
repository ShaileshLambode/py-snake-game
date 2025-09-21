import time
import turtle

import food
from snake import Snake
from turtle import Turtle , Screen
from food import Food
from scoreboard import Score

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game !!")
screen.tracer(0)

snake = Snake()
food = Food()
score1 = Score()

score1.show_score()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    screen = Screen()
    screen.listen()
    screen.onkey(key='Up', fun=snake.move_up)
    screen.onkey(key='Down', fun=snake.move_down)
    screen.onkey(key='Left', fun=snake.move_left)
    screen.onkey(key='Right', fun=snake.move_right)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.expand()
        score1.add_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        # game_on = False
        snake.reset()
        score1.reset()
        # score1.game_over()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            score1.reset()
            # game_on = False
            # score1.game_over()
screen. exitonclick()