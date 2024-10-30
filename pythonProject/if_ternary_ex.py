"""
Ternary:

Ex1: input a height between 0.1 - 2.8
        print 'You are tall (if height > 1.8)
        print 'You aren't tall (if height <= 1.8)
"""

height: float = float(input('Please input a height (between 0.1 - 2.8): '))

if height > 1.8:
    print(f'You are tall person, your height is: {height} meters!')

else:
    print(f'You arent a tall person, your height is: {height} meters!')



"""
Ex2. input a number between 0 -99
        print 'The number is 1 digit
        print 'The number is 2 digits
"""
digit: int = int(input('Please enter a number(between 0 - 99): '))

if digit % 2 == 0:
    print('The number is 1 digit')

else:
    print('The number is 2 digits!')
