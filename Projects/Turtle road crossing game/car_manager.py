from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.total_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        if r.randint(1, 4) == 2:
            t = Turtle("square")
            t.shapesize(0.5, 1.5)
            t.penup()
            t.color(r.choice(COLORS))
            t.start_position = r.randint(-250, 250)
            t.goto(300, t.start_position)
            self.total_cars.append(t)

    def move_cars(self):
        for car in self.total_cars:
            car.bk(self.speed)

    def move_fast(self):
        self.speed += MOVE_INCREMENT