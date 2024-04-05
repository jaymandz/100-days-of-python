def turn_right():
    for t in range(3): turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    elif wall_on_right():
        move()