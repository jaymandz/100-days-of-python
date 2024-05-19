from random import randint
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title='Make your bet',
    prompt='Which turtle will win the race? Enter a color: ',
)

colors = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'purple',
]

turtles = []
for c in range(len(colors)):
    t = Turtle(shape='turtle')
    t.color(colors[c])
    t.penup()
    t.goto(x=-230, y=200/len(colors)*c-100)
    turtles.append(t)

is_race_over = False
while not is_race_over:
    for t in turtles:
        t.forward(randint(1, 10))
        if t.xcor() >= 230:
            winner = t.color()[0]
            is_race_over = True

if winner == user_bet: status = 'won'
else: status = 'lost'

print(f'You\'ve {status}! The {winner} turtle is the winner!')

screen.exitonclick()