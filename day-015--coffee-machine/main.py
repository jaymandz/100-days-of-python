def purchase_coffee(prompt, coins, recipes, resources):
    # 4 arguments!!
    total_payment = coins['num_quarters'] * 0.25 + \
      coins['num_dimes'] * 0.1 + \
      coins['num_nickels'] * 0.05 + \
      coins['num_pennies'] * 0.01

    price = recipes[prompt]['price']
    if total_payment < price:
        print('Sorry that\'s not enough money. Money refunded.')
    else:
        resources['water'] -= recipes[prompt]['water']
        resources['coffee'] -= recipes[prompt]['coffee']
        resources['milk'] -= recipes[prompt]['milk']
        resources['money'] += price

        if total_payment > price:
            print('Here is ${:.2f} in change.'.format(total_payment - price))
        
        print(f'Here is your {prompt} Enjoy!')
    
    return resources

recipes = {
    'espresso': {
        'water': 50,
        'coffee': 18,
        'milk': 0,
        'price': 1.5,
    },
    'latte': {
        'water': 200,
        'coffee': 24,
        'milk': 150,
        'price': 2.5,
    },
    'cappuccino': {
        'water': 250,
        'coffee': 24,
        'milk': 100,
        'price': 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 2.5,
}

choices = [
    'espresso',
    'latte',
    'cappuccino',
    'report',
    'off',
]

while True:
    prompt = None
    while prompt not in choices:
        prompt = input('What would you like? (espresso/latte/cappuccino) ')
    
    if prompt == 'off': break
    elif prompt == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print('Money: ${:.2f}'.format(resources['money']))
    elif prompt in ['espresso', 'latte', 'cappuccino']:
        if recipes[prompt]['water'] > resources["water"]:
            print('Sorry there is not enough water.')
        elif recipes[prompt]['coffee'] > resources["coffee"]:
            print('Sorry there is not enough coffee.')
        elif recipes[prompt]['milk'] > resources["milk"]:
            print('Sorry there is not enough milk.')
        else:
            coins = {}
            print('Please insert coins.')
            coins['num_quarters'] = int(input('How many quarters? '))
            coins['num_dimes'] = int(input('How many dimes? '))
            coins['num_nickels'] = int(input('How many nickels? '))
            coins['num_pennies'] = int(input('How many pennies? '))

            resources = purchase_coffee(prompt, coins, recipes, resources)