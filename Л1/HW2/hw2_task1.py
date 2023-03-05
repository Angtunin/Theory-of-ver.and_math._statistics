"""
Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз.
Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
"""
# решение с помощью формулы биноминального распределения P(X = k) = C(n, k) * p^k * (1-p)^(n-k)
p = 0.8
n = 100
k = 85
from math import factorial

def combination(k, n):
    comb_event = factorial(n) // (factorial(k) * factorial(n - k))
    return comb_event

print(f'C(100, 85) = {combination(85, 100)}')

print(f'P(X = 85) = {(combination(85, 100)) * (p ** k) * ((1 - p) ** (n - k))}')