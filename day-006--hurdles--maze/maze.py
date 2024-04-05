# You need to go to https://reeborg.ca/index_en.html and select the Maze
# puzzle for this code to work.

def turn_right():
    for t in range(3): turn_left()

while not at_goal():
    if wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move()
    else:
        turn_right()
        move()