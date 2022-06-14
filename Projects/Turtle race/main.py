import turtle as t

draw = t.Turtle()


def front():
    draw.fd(50)


def back():
    draw.bk(50)


def right():
    draw.right(10)


def left():
    draw.left(10)


def clear():
    draw.home()
    draw.clear()


screen = t.Screen()
screen.listen()
screen.onkey(clear, "c")
screen.onkey(front, "w")
screen.onkey(back, "s")
screen.onkey(right, "d")
screen.onkey(left, "a")
screen.exitonclick()
