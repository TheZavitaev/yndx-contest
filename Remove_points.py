"""
Гоша решил убрать из статистики дни, когда ничего в «‎Черепашеньке» не заработал и не проиграл.
Дан список заработанных очков. Нужно удалить из него нули. Дополнительную память больше O(1) использовать нельзя.

Формат ввода
В первой строке - одно число n. Во второй - n целых чисел через пробел.

Формат вывода
Напечатайте очки за все дни, где выигрыш был отличен от нуля.
"""

n = int(input())
result_days = list(map(int, input().split()))
days = []

for i in result_days:
    if i != 0:
        days.append(i)

print(*days)