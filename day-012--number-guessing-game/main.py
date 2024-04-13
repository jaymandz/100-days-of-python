import random

print('Welcome to the Number Guessing Game!')

random_number = random.randint(1, 100)
print('I\'m thinking of a number between 1 and 100.')

difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
if difficulty == 'easy': num_attempts = 10
elif difficulty == 'hard': num_attempts = 5

while num_attempts > 0:
    print(f'You have {num_attempts} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))

    if guess == random_number:
        print(f'You got it! The answer was {random_number}.')
        break
    else:
        if guess > random_number: print('Too high.')
        elif guess < random_number: print('Too low.')

        num_attempts -= 1
        if num_attempts > 0: print('Guess again.')
        else: print('You\'ve run out of guesses, you lose.')