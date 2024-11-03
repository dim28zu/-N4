def add_numbers(a, b):
    return a + b

try:
    a = float(input('Enter 1st number: '))
    b = float(input('Enter 2nd number: '))
    print(f'Sum of {a} and {b} is {add_numbers(a, b)}')
except ValueError:
    print("Please enter valid numbers.")
