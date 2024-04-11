def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

num1 = float(input('What\'s the first number? '))
for o in operations: print(o)

while True:
    operation = input('Pick an operation: ')
    num2 = float(input('What\'s the next number? '))

    answer = operations[operation](num1, num2)
    print(f'{num1} {operation} {num2} = {answer}')

    yn = input(f'Type \'y\' to continue calculating with {answer}, or type \'n\' to start a new calculation: ')
    if yn == 'y': num1 = answer
    elif yn == 'n': num1 = float(input('What\'s the first number? '))