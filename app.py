def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def divide(a, b):
    if b != 0:
        return a / b

print('Welcome to the simple calculator!')
print('Available operations: add, sub, mul, div')

operation = input('Enter the operation: ')
num1 = float(input('a: '))
num2 = float(input('b: '))

if operation == 'add':
    print(f'Result: {add(num1, num2)}')
elif operation == 'sub':
    print(f'Result: {subtract(num1, num2)}')
elif operation == 'div':
    print(f'Result: {divide(num1, num2)}')
