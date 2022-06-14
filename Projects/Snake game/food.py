from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(10)
        self.color("green")
        self.penup()
        self.shape("turtle")
        self.shapesize(0.5)
        self.refresh_food()

    def refresh_food(self):
        xp = random.randint(-280, 280)
        yp = random.randint(-280, 280)
        self.goto(xp, yp)
