"""
Вася решил запутать маму —– делать дела в обратном порядке. Список его дел теперь хранится в двусвязном списке.
Напишите функцию, которая вернёт список в обратном порядке.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать только функцию,
которая принимает на вход голову двусвязного списка и возвращает голову перевернутого списка.
Ниже дано описание структуры, которая задаёт вершину списка.
Внимание! Решение надо отправлять только в виде файла с расширением, которое соответствует вашему языку.
Иначе даже корректно написанное решение не пройдет тесты.

Формат ввода
Функция принимает на вход единственный аргумент — голову двусвязного списка.
Python:
Если вы пишете на Python, функция должна называться solution и принимать на вход вершину node.
Узел списка описывается следующим классом:

class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

Формат вывода
Функция должна вернуть голову развернутого списка.
Примечания
Решение нужно отправлять в виде файла с расширением соответствующем вашему языку программирования.
Нужно выбирать компилятор make. Для Java файл должен называться Solution.java
Для остальных языков программирования это имя использовать нельзя (имя solution тоже).
"""


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.value


def solution(head):

    if head is None:
        return head

    head.next, head.prev = head.prev, head.next

    if head.prev is None:
        return head

    return solution(head.prev)