# Задача 0001
# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal
import sys

try:
    number = Decimal(input('Введите число: '))
    accuracy = input('Введите точность: ')
except ValueError:
    print('Вы ввели недопустимый символ. Программа завершает работу... ')
    sys.exit()
if not ('1' in accuracy) or not ('0' in accuracy) or not('.' in accuracy):
    print('Для указания точности допускаются только символы "0" "1" "." Программа завершает работу... ')
    sys.exit()


print(f'Вы ввели число {number} с точностью {accuracy}')
accuracy = len(accuracy.split('.')[1])
print('=>', round(number, accuracy))
