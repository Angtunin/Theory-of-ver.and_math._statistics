"""
В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.
Какова вероятность того, что все извлеченные детали окрашены?
"""
from math import factorial

def combination(k, n):
    comb_event = factorial(n) // (factorial(k) * factorial(n - k))
    return comb_event
print(f'Число благоприятных исходов = {combination(3, 9)}')
print(f'Число всех исходов = {combination(3, 15)}')
print(f'вероятность того, что все извлеченные детали окрашены = {combination(3, 9) / combination(3, 15)}')