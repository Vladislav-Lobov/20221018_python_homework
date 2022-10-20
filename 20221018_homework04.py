# Задача 0004
# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x = 0

import sys
from random import randint
from sympy import Symbol, Poly


for j in [1, 2]:  # цикл для записи двух файлов

    try:
        k = int(input('Введите степень k: '))
    except ValueError:
        print('Допускаются только натуральные числа. Программа завершает работу... ')
        sys.exit()
    if k < 1:
        print('Допускаются только положительные числа. Программа завершает работу... ')
        sys.exit()

    # чтобы получить многочлен k-степени, индекс с номером 0 не должен быть нулем:
    array = [randint(1,100)] + [str(randint(0, 100)) for i in range(k)]
      

    print(f'Список случайных коэффициентов: {array}')

    x = Symbol('x')
    result = str(Poly(array, x))
    print(f'Работа функции Poly из модуля sympy: {result}')
    result = result[5:-17:]
    result = result.replace('**', '^')
    result = result.replace('*', '')
    result = result + ' = 0'
    print(f'Результат работы программы: {result}')

    with open(f'file{j}.txt', 'w') as data:
        data.write(result)
