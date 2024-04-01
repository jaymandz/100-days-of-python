print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))
payment = round(bill * (tip / 100 + 1) / people, 2)
print('Each person should pay: ${:.2f}'.format(payment))
#print(f'Each person should pay: ${payment}')
# Tbh I did not expect that payment would display 33.6 instead of 33.60. 