# I just strictly followed Angela Yu's flowchart. I'll put in a story of my
# own later when I feel like it.

print('Welcome to Treasure Island. Your mission is to find the treasure.')

direction = input('left or right? ').lower()
if direction == 'left':
    action = input('swim or wait? ').lower()
    if action == 'wait':
        door = input('which door? blue, red, or yellow? ').lower()
        if door == 'blue':
            print('Eaten by beasts. Game Over.')
        elif door == 'red':
            print('Burned by fire. Game Over.')
        elif door == 'yellow':
            print('You Win!')
        else:
            print('Game Over.')
    else:
        print('Attacked by trout. Game Over.')
else:
    print('Fall into a hole. Game Over.')