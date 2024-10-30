num: int = int(input('Please enter a number: '))
sum_dig = 0

print(num, ': ', end='')

while num > 0:
    units = num % 10
    sum_dig += units
    num = num // 10

print(f'')