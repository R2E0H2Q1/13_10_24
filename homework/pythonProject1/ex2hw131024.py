print('Part 2: Loops')
print()

"""6. Take a natural number n and print all the integers from n to 1 in descending order.
- Example: if 5 = n is entered, it will be printed: 1, 5, 4, 3, 2"""

n: int = int(input(f'Please enter a number: '))

print(f'This is an example of a reversed list:', end=' ')#The print needs to be added outside the loop so it doesn't
#run everytime and prints all numbers individually.
for i in range(n, 0, -1): #the -1 reverses the order
    print(i, end=' ') #prints a reversed list of all numbers from the value of 'n' up to 0.
print()
"""7. Take two numbers and print all the even numbers between them.
- Example: If 4 and 10 were received, the following will be printed: 4, 6, 8, 10
- If 7 and 13 were taken, the following will be printed: 12, 10, 8"""

fnum: int = int(input(f'Enter a number: '))
snum: int = int(input(f'Enter a second number: '))

if snum < fnum: #checks if the second number if less that the first number
    fnum, snum = snum, fnum #swaps the positions of the numbers

print(f'The even numbers between {fnum} and {snum} are: ', end=' ')

for i in range(fnum, snum):
    if i % 2 == 0: #checks the even numbers
        print(i, end=' ')
print()

"""8. Pick a positive number n and print all the numbers up to n that are divisible by 3 or 5 or both.
- Example: if 15 = n is entered, it will be printed: 15, 3, 5, 6, 9, 10, 12"""

print(f'The numbers divisible by 3 and 5 from the sequence 1 to {n} are: ', end=' ')

for i in range(1, n +1):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=' ')
print()

"""9. Select the number n and print all the numbers that are multiples of 7 to n
- Example: if 30 = n is entered, the following will be printed: 14, 21, 7, 28"""

print(f'The numbers divisible by 7 are: ', end=' ')

for i in range(1, n +1):
    if i % 7 == 0:
        print(i, end=' ')