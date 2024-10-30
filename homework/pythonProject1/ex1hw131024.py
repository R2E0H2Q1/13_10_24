print('Part 1: Conditionals')
print()

"""1. Calculate a decimal number, if it is greater than 10 - print the difference between it and 10, otherwise print it multiply by 10.
- Example: If the number 15 is entered, 5 will be printed (because 15 - 10 = 5).
- If the number 8 is received, 80 will be printed (because 8 * 10 = 80)."""

checkdigit = 10
recorddigt: int = int(input('Please enter a number(2 digits maximum: '))

if recorddigt > checkdigit:
    print(f'The difference between {recorddigt} and {checkdigit} is: {recorddigt - checkdigit}')

else:
    print(f'{recorddigt} multiplied by {checkdigit} is equal to: {recorddigt * checkdigit}')
print()

""" 2. Enter three numbers and print their sum only if the sum is greater than 100 - otherwise print
- "The amount is less than 100-"
- Example: If the numbers 30, 40 and 50 were received, 120 will be printed (because the sum is greater than 100).
- If the numbers 10, 20 and 30 were received, "the amount is less than -100" will be printed"""

check_digit = 100
total = 0

for _ in range(3):
    while True:
        times3 = int(input('Please enter a number(2 digits maximum: '))
        total += times3
        break

if total > check_digit:
    print(f'The sum is greater than 100. The amount is: {total}')

else:
    print(f'The amount is less than 100!')
print()

"""3. *Bonus/permission: enter two decimals and print the larger fraction. If the fractions are equal, print "equal."
- Example: If the numbers 3.75 and 9.5 were received, 0.75 will be printed. Hint, use int
- If the numbers 2.5 and 1.5 were received, "equal" will be printed."""


""" 4. Enter age and make sure it is correct (above 0 and below 120). If it is incorrect, print "Incorrect age."
- Example: If the age is entered, 25 will be printed
- If the age is entered, 130 will be printed "incorrect age."""

age: int = int(input('Please enter your age(Between 0 and 120): '))

if 0 < age <= 120:
    print(f'Your age is {age}!')
else:
    print('Incorrect age!')
print()

"""5. Calculate a three-digit number and print its middle digit.
- Example: If the number is entered, 149 will be printed. 4
- If the number is entered, 567 will print 6."""

num3s: int = int(input('Please enter a 3 digits number: '))

if 100 <= num3s <= 999: #checks if the provided number is indeed 3 digits long.
    middle_dgt = str(num3s)[1] #converts the provided number into a string and extracts the index number 1
    print(f'The middle digit of {num3s} is {middle_dgt}')
else:
    print('The number must be three-digits!')