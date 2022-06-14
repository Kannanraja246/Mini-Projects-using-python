import time
import turtle as t
from pedal import Paddle
from ball import Ball
import split_line
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(800, 500)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
line = split_line
board = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_down, "s")

line.create_line()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if board.r_score >= 10:
        game_is_on = False
        board.r_match_won()
    if board.l_score >= 10:
        game_is_on = False
        board.l_match_won()
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() <= -350:
        ball.bounce_x()
        # board.time()
    if ball.xcor() > 390:
        ball.reset_position()
        board.l_point()
    if ball.xcor() < -390:
        ball.reset_position()
        board.r_point()

screen.exitonclick()