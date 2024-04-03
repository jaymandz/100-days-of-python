import random

# Copied the ASCII art from the starter code.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_hand = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if player_hand == 0: print(rock)
elif player_hand == 1: print(paper)
elif player_hand == 2: print(scissors)

print('Computer chose:')
computer_hand = random.randint(0, 2)
if computer_hand == 0: print(rock)
elif computer_hand == 1: print(paper)
elif computer_hand == 2: print(scissors)

if player_hand == computer_hand: print('Draw')
elif player_hand == 0 and computer_hand == 1 or \
  player_hand == 1 and computer_hand == 2 or \
  player_hand == 2 and computer_hand == 0: print('You lose')
elif player_hand == 0 and computer_hand == 2 or \
  player_hand == 1 and computer_hand == 0 or \
  player_hand == 2 and computer_hand == 1: print('You win')
else: print('You typed an invalid number!')