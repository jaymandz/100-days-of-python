# I took the "Expert" difficulty, this is why my solution looks very
# different from Angela Yu's. 😎

import os, random

def total(hand):
    t = 0
    for card in hand:
        if card in ['ten', 'jack', 'queen', 'king']: t += 10
        elif card == 'two': t += 2
        elif card == 'three': t += 3
        elif card == 'four': t += 4
        elif card == 'five': t += 5
        elif card == 'six': t += 6
        elif card == 'seven': t += 7
        elif card == 'eight': t += 8
        elif card == 'nine': t += 9
        elif card == 'ace':
            if t > 21: t += 1
            else: t += 11
    return t

def hit(): return random.choice(cards)

def print_player_hand():
    t = total(player_hand)
    print(f'Your cards are: {", ".join(player_hand)}. Total is {t}.')

def print_dealer_hand():
    t = total(dealer_hand)
    print(f'Dealer\'s cards are: {", ".join(dealer_hand)}. Total is {t}.')

cards = [
    'ace',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'jack',
    'queen',
    'king',
]

dealer_hand = []
player_hand = []

while True:
    player_hand = [hit(), hit()]
    dealer_hand = [hit(), hit()]

    print_player_hand()
    print(f'The dealer\'s cards are: {dealer_hand[0]}, [?].')

    while True:
        action = None
        while action not in ['h', 's']:
            action = input('Enter "h" to hit, "s" to stand: ')
        if action == 'h':
            player_hand.append(hit())
            if total(player_hand) > 21: break
            else: print_player_hand()
        elif action == 's': break
    
    player_total = total(player_hand)
    dealer_total = total(dealer_hand)
    if player_total <= 21: 
        while dealer_total < 17:
            dealer_hand.append(hit())
            dealer_total = total(dealer_hand)
        
    print_player_hand()
    print_dealer_hand()
    if player_total > 21: print('Bust! Dealer wins!')
    elif dealer_total > 21: print('Bust! Player wins!')
    elif dealer_total > player_total: print('Dealer wins!')
    elif dealer_total < player_total: print('Player wins!')
    else: print('Draw.')
    
    yn = None
    while yn not in ['y', 'n']: yn = input('Deal again? ("y" or "n") ')
    os.system('cls' if os.name == 'nt' else 'clear')
    if yn == 'n':
        print('Bye.')
        break