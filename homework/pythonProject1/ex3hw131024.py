print('3. Data processing:')
print()

"""11. Add numbers until the number 0 is received, print the sum of the negative numbers received.
- Example: If the numbers: -3, 91, -5, -2, 4 and 0 were received, it will be printed: -10 (because -3 + -5 + -2 = -10)."""

total = 0

while True:
    numbs: int = int(input('Enter a number: '))
    if numbs == 0: #when the user enters 0, it will exit.
        break
    if numbs < 0: #will check if the provided number is negative
        total += numbs #will sum the received negative numbers
print(f' {total} is the sum of the provided negative numbers!')
print()

"""12. Make a list of 10 numbers and print the numbers in reverse order.
- Example: If: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 were received, the following will be printed: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1."""

num_list = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]

print(f'This is a reversed list: {num_list[::-1]}')
print()

"""13. collect a series of numbers until the number 0 is received, and print how many of the entered numbers are prime.
- Example: If the numbers: 0, 2, 3, 4, 5, 0 are taken, 3 will be printed (because 2, 3 and 5 are prime)."""
# Prime numbers are the ones that can be divided by himself and 1

counter = 0
divider = 2

while True:
    nums: int = int(input('Enter a number(Exit = 0): '))
    if nums == 0:
        break
    if divider < nums: #will check if the provided number is prime
        counter += 1 #will sum how many prime numbers were entered
print(f' {counter} is the sum of the provided prime numbers!')
print()

"""14. Take 5 numbers and print their average, and also print the amount of numbers larger than the average.
- Example: If the numbers were taken: 10, 20, 30, 40, 50, the average is 30, and there are 2 large numbers
than the average. (50 40,)"""

five_num = [] #creates an empty list

for _ in range(5): #provides the amount of times a number must be request.
    while True:
        digit = int(input('Please enter a number: ')) #request the input
        five_num.append(digit)
        break
average = sum(five_num) / len(five_num) #calculates the average on the list
print(f'The average for the 5 provided numbers is: {average}')


big_num = [digit for digit in five_num if digit > average] #checks which on the provided numbers is bigger than average.
lgr = len(big_num) #count how many numbers are bigger than average.
print(f'There are {lgr} numbers larger that the average: {big_num}')
print()

"""15. Collect two numbers and print the result of their division using only reductions.
- Example: if the numbers 20 and 5 were taken - the result is 4 (because 20/5 = 4)."""

two_num = []

for _ in range(2):
    while True:
        num = int(input('Provide a number: '))
        two_num.append(num)
        break

indx0 = two_num[0]
indx1 = two_num[1]


if indx0 == 0:
    print("Division by zero is not allowed.")
else:
    outcome = 0
    while indx0 >= indx1:
        indx0 -= indx1
        outcome += 1

    print(f'The result of the division of {two_num} is: {outcome}')
