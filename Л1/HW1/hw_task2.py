"""
На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код,
откроет дверь с первой попытки?
"""
from math import factorial

def combination(k, n):
    comb_event = factorial(n) // (factorial(k) * factorial(n - k))
    return comb_event
print(f'Число исходов для 3-х цифр из 10 = {combination(3, 10)}')
c = combination(3, 10)
# Количество благоприятных исходов = 1
print(f'вероятность открыть дверь с первой попытки = {1 / c}')

