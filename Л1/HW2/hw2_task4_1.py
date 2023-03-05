"""
В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые?
"""
from math import factorial

def combination(k, n):
    comb_event = factorial(n) // (factorial(k) * factorial(n - k))
    return comb_event

p1 = combination(2, 7) / combination(2, 10)
print(f'Вероятность достать только белые шары из ящика 1 p1 = {p1}')

p2 = combination(2, 9) / combination(2, 11)
print(f'Вероятность достать только белые шары из ящика 2 p1 = {p2}')

p = p1 * p2
print(f'Вероятность достать только белые шары из двух ящиков p = {p}')


