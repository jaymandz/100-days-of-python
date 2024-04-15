import json, os, random

def increment_and_print_score(score):
    print(f"You're right! Current score: {score + 1}.")
    return score + 1

game_data = json.load(open(os.path.dirname(__file__)+'/data.json', 'r'))

score = 0
a = random.choice(game_data)

while True:
    while (b := random.choice(game_data)) == a: pass

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

    choice = None
    while choice not in ['a', 'b']:
        choice = input('Who has more followers? Type "A" or "B": ').lower()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == 'a' and a['follower_count'] > b['follower_count']:
        score = increment_and_print_score(score)
    elif choice == 'b' and a['follower_count'] < b['follower_count']:
        a = b
        score = increment_and_print_score(score)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break