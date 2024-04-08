import random

hangmen = [
    '''
  +---+
  |   |
  0   |
      |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  0   |
  |   |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  0   |
 /|   |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========
    ''',
    '''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
    ''',
]

word_list = [
    'aardvark',
    'baboon',
    'camel',
]

random_word = random.choice(word_list)

current_answer = ['_' for l in random_word]
num_mistakes = 0

while '_' in current_answer and num_mistakes < 6:
    guess = input('Guess a letter: ').lower()
    if guess not in random_word:
        print(hangmen[num_mistakes])
        num_mistakes += 1
    else:
        for l in range(len(random_word)):
            if random_word[l] == guess: current_answer[l] = guess
        print(' '.join(current_answer))

if num_mistakes < 6: print('You win.')
else: print('You lose.')