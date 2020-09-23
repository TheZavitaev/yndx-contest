# 34772869
"""
В качестве второго задания финального проекта нужно написать программу,
которая определяет, есть ли цикл в связном списке.
На вход функция принимает голову списка, на выходе должна выдать True,
если в списке содержится цикл, иначе — False. Размер дополнительной памяти,
к которой обращается функция, не должен превышать О(1).

Формат ввода
В этой задаче вам нужно реализовать только функцию с решением,
считывать входные данные не нужно.
Функция должна принимать на вход голову связного списка.
Класс, представляющая узел списка выглядит так:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __repr__(self):
        return self.value
Ваша функция должна называться hasCycle.

Формат вывода
Функция должна возвращать булево значение

Примечания
При отправке нужно выбирать компилятор make и загружать решение в виде файла.
Файл может быть назван любым именем, кроме solution.py
Расширение .py должно присутствовать обязательно.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def hasCycle(head):
    if head is not None:
        slow, fast = head, head

        while fast.next is not None and fast.next.next is not None:
            slow, fast = slow.next, fast.next.next

            if slow == fast:
                return True

        return False
