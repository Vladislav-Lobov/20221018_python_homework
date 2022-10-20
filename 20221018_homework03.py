# Задача 0003
# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

import sys
from random import randint

try:
    size_array = int(input('Введите размер списка элементов: '))
except ValueError:
    print('Допускаются только натуральные числа. Программа завершает работу... ')
    sys.exit()
if size_array < 1:
    print('Допускаются только положительные числа. Программа завершает работу... ')
    sys.exit()

array = [randint(0, 9) for i in range(size_array)]
print(f'Последовательность из {size_array} случайных чисел: {array}')
result_array = [i for i in array if array.count(i) == 1]
print(f'Список неповторяющихся элементов: {result_array}')
