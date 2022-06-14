from turtle import Turtle


def create_line():
    y = 20
    for i in range(13):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.turtlesize(1.5, 0.5)
        t.goto(0, -250 + y)
        y += 40
