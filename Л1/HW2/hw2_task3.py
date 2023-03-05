"""
Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
"""
# решение с помощью формулы биноминального распределения P(X = k) = C(n, k) * p^k * (1-p)^(n-k)
p = 0.5
n = 144
k = 70
from math import factorial

def combination(k, n):
    comb_event = factorial(n) // (factorial(k) * factorial(n - k))
    return comb_event

print(f'C(144, 70) = {combination(70, 144)}')

print(f'P(X = 70) = {(combination(70, 144)) * (p ** k) * ((1 - p) ** (n - k))}')