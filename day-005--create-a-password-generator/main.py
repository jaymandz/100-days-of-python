import random

print('Welcome to the PyPassword Generator!')
num_letters = int(input('How many letters would you like in your password?\n'))
num_symbols = int(input('How many symbols would you like?\n'))
num_numbers = int(input('How many numbers would you like?\n'))

# I'm not gonna bother implementing these three as lists.
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
symbols = '`~!@#$%^&*()-_=+[{\|}];:\'",<.>/?'
numbers = '01234567689'

length = num_letters + num_symbols + num_numbers
password = ''
for c in range(0, length):
    types = []
    if num_letters > 0: types.append(0)
    if num_symbols > 0: types.append(1)
    if num_numbers > 0: types.append(2)

    random_type = random.choice(types)
    if random_type == 0:
        password += random.choice(letters)
        num_letters -= 1
    elif random_type == 1:
        password += random.choice(symbols)
        num_symbols -= 1
    elif random_type == 2:
        password += random.choice(numbers)
        num_numbers -= 1
    
print(f'Here is your password: {password}')