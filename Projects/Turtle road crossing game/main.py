import time
import turtle as t
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = CarManager()
player = Player()
board = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

player.start()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()
    for car in cars.total_cars:
        if car.distance(player) <= 15:
            game_is_on = False
            board.game_over()
    if player.ycor() == 280:
        player.start()
        board.level()
        cars.move_fast()


screen.exitonclick()