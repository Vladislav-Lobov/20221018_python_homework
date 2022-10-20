# Задача 0002
# Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.

import sys


def is_simple(n):
    for j in range(2, int(n ** 0.5)):
        if n % j == 0:
            return False
    else:
        return True


try:
    number = int(input('Введите N: '))
except ValueError:
    print('Допускаются только натуральные числа. Программа завершает работу... ')
    sys.exit()
if number < 1:
    print('Допускаются только положительные числа. Программа завершает работу... ')
    sys.exit()

print(f'Простые множители числа {number}:',end=' ')
res_array = []
for i in range(2, number + 1):
    if is_simple(i):
        while number % i == 0:
            res_array.append(i)
            number = number // i
print(res_array)
