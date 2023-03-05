"""
В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что ровно два мяча белые?
"""
from math import factorial

def combination(k, n):
    comb_event = factorial(n) // (factorial(k) * factorial(n - k))
    return comb_event
"""
расчёт вероятности это сумма трёх вероятностей p1 (1б из 1я и 1б из 2я) + p2 (2б из 1я и 0б из 2я) +
p3 (0б из 1я и 2б из 2я)
"""
p1 = (combination(1, 7) / combination(1, 10)) * (combination(1, 9) / combination(1, 11))
print(f'p1 = {p1}')

p2 = (combination(2, 7) / combination(2, 10)) * (combination(2, 2) / combination(2, 11))
print(f'p2 = {p2}')

p3 = (combination(2, 3) / combination(2, 10)) * (combination(2, 9) / combination(2, 11))
print(f'p3 = {p3}')

p = p1 + p2 + p3
print(f'Вероятность достать только 2 белых шара из двух ящиков p = {p}')

