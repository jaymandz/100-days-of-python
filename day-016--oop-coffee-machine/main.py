from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
m = Menu()
mm = MoneyMachine()

choices = ['espresso', 'latte', 'cappuccino', 'report', 'off']

while True:
    prompt = 'x'
    while prompt not in choices:
        prompt = input(f'What would you like? ({m.get_items()}) ')
    
    if prompt == 'off': break
    elif prompt == 'report':
        cm.report()
        mm.report()
    else:
        if not (drink := m.find_drink(prompt)): continue
        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost): cm.make_coffee(drink)