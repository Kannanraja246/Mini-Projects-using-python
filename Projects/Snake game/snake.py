import turtle as t
screen = t.Screen()
n = 3


class Snake:

    def __init__(self):
        self.seg = []
        self.n = 3
        self.p = 0
        self.snake_body()
        # self.snake_movement()

    def snake_body(self):
        screen.tracer(0)
        for i in range(self.n):
            snakes = t.Turtle("square")
            snakes.color("white")
            snakes.penup()
            snakes.goto(x=self.p, y=0)
            self.p += - 20
            self.seg.append(snakes)
            self.seg[0].color("red")
        screen.update()

    def add_body(self):
        xp = self.seg[-1].xcor()
        yp = self.seg[-1].ycor()
        screen.tracer(0)
        snakes = t.Turtle("square")
        snakes.color("white")
        snakes.penup()
        snakes.goto(x=xp, y=yp)
        self.seg.append(snakes)
        screen.update()

    def snake_movement(self):
        for move in range(len(self.seg) - 1, 0, -1):
            xp = self.seg[move - 1].xcor()
            yp = self.seg[move - 1].ycor()
            self.seg[move].goto(xp, yp)
        self.seg[0].fd(20)

    def clear_snake(self):
        for i in self.seg:
            i.goto(100, 1000)
        self.seg.clear()
        self.p = 0
        self.snake_body()

    def right(self):
        if self.seg[0].heading() != 180:
            self.seg[0].seth(0)

    def left(self):
        if self.seg[0].heading() != 0:
            self.seg[0].seth(180)

    def up(self):
        if self.seg[0].heading() != 270:
            self.seg[0].seth(90)

    def down(self):
        if self.seg[0].heading() != 90:
            self.seg[0].seth(270)
