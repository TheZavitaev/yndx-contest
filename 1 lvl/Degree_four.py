"""
Вася на уроке математики проходил степени. Он хочет написать программу,
которая определяет, будет ли положительное целое число степенью четверки.

Формат ввода
На вход подается целое число в диапазоне от 1 до 10000.

Формат вывода
True, если число является степенью четырех, False - в обратном случае.
"""
from math import log
n = int(input())

Logn = log(n, 4)

print(Logn == int(Logn))
