from turtle import Screen, Turtle

tortuga = Turtle()

screen = Screen()

def forward(): tortuga.forward(10)
def back(): tortuga.back(10)
def left(): tortuga.left(5)
def right(): tortuga.right(5)
def clear(): screen.reset()

screen.listen()
screen.onkey(forward, 'w')
screen.onkey(back, 's')
screen.onkey(left, 'a')
screen.onkey(right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()