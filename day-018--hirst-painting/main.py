import random, turtle

colors = [
    (171, 158, 33),
    (99, 6, 51),
    (75, 94, 173),
    (232, 209, 73),
    (10, 35, 127),
    (178, 104, 155),
    (215, 89, 34),
    (105, 123, 210),
    (26, 96, 40)
]

turtle.colormode(255)

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()

for row in range(-225, 226, 50):
    timmy.setposition(-225, row)
    for column in range(10):
        timmy.pencolor(random.choice(colors))
        timmy.dot(20)
        timmy.forward(50)

timmy.home()

screen = turtle.Screen()
screen.exitonclick()