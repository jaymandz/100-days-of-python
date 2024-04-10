# I'm not on Repl so I needed another way to clear the console.

import os

bidders = []
hbi = -1

print('Welcome to the secret auction program.')
while True:
    name = input('What is your name? ')
    bid = int(input('What\'s your bid? $'))
    bidders.append({ 'name': name, 'bid': bid })

    if hbi == -1 or bid > bidders[hbi]['bid']: hbi = len(bidders) - 1

    yn = input('Are there any other bidders? Type \'yes\' or \'no\'. ')
    os.system('cls' if os.name == 'nt' else 'clear')
    if yn == 'no':
        print(f'The winner is {bidders[hbi]["name"]} with a bid of {bidders[hbi]["bid"]}.')
        break