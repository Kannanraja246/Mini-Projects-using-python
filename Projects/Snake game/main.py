import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")

screen.tracer(0)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(scoreboard.move_speed)
    snake.snake_movement()
    # scoreboard.score()
    # scoreboard.high_sore()
    if snake.seg[0].distance(food) < 15:
        food.refresh_food()
        scoreboard.actual_score()
        snake.add_body()
    for seg in snake.seg[1:-1]:
        if snake.seg[0].distance(seg) < 10:
            scoreboard.high_score()
            snake.clear_snake()

    if snake.seg[0].xcor() > 280 or snake.seg[0].xcor() < -280 or snake.seg[0].ycor() > 280 or snake.seg[0].ycor()\
            < -280:
        scoreboard.high_score()
        snake.clear_snake()

screen.exitonclick()
