from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.levels = 0
        self.level()

    def level(self):
        self.clear()
        self.levels += 1
        self.goto(-250, 270)
        self.write(f"Level {self.levels}", True, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, "center", FONT)
