from turtle import Turtle
FONT = ("Courier", 20, "bold")
with open("highscore_data.txt", mode="r") as h:
    H = h.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.s = 0
        self.hs = int(H)
        self.score()
        self.move_speed = 0.5

    def score(self):
        self.clear()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.speed(10)
        self.goto(-10, 270)
        self.write(f"Score: {self.s}  High Score {self.hs}", False, "center", FONT)

    def actual_score(self):
        self.clear()
        self.s += 1
        self.move_speed *= 0.9
        self.write(f"Score: {self.s}  High Score {self.hs}", False, "center", FONT)

    def high_score(self):
        if self.s > self.hs:
            self.hs = self.s
            with open("highscore_data.txt", mode="w") as high:
                high.write(str(self.hs))
        self.s = 0
        self.score()
