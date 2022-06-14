import turtle as t
import random as r
screen = t.Screen()
screen.setup(width=600, height=500)
color = ["red", "yellow", "green", "orange", "blue", "purple"]
user_bet = screen.textinput(title="set your BET", prompt=f"which color turtle will win?{color}")
tur = []
for i in range(0, 6):
    new_turtle = t.Turtle("turtle")
    new_turtle.speed(10)
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=-150 + (i * 50))
    tur.append(new_turtle)

if user_bet in color:
    race = True
else:
    print(f"Please select color from the following list, better luck next time\n{color}")
    race = False
while race:
    for x in tur:
        if x.xcor() > 280:
            race = False
            winner = x.pencolor()
            if user_bet == winner:
                print("You win!")
            else:
                print("You lose")
            print(f"The winner is {winner} color turtle")
        steps = r.randint(0, 10)
        x.fd(steps)


screen.exitonclick()
