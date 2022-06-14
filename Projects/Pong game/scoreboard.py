from turtle import Turtle
import time


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.position()

    def position(self):
        self.clear()
        self.goto(100, 180)
        self.write(self.r_score, True, "center", ("arial", 50, "normal"))
        self.goto(-100, 180)
        self.write(self.l_score, True, "center", ("arial", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.position()

    def r_point(self):
        self.r_score += 1
        self.position()

    def r_match_won(self):
        self.goto(0, 0)
        self.write("Right side won the match", True, "center", ("arial", 40, "normal"))

    def l_match_won(self):
        self.goto(0, 0)
        self.write("Left side won the match", True, "center", ("arial", 40, "normal"))