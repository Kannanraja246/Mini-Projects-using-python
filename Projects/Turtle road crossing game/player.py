from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Green")
        self.shape("turtle")
        self.penup()
        self.start()

    def move(self):
        self.fd(MOVE_DISTANCE)

    def start(self):
        self.seth(90)
        self.goto(STARTING_POSITION)

