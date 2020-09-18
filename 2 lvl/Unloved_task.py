"""
LinkedList
Вася размышляет, что бы такое из списка не делать. Но, кажется, все пункты очень важные!
Вася решает загадать число и удалить дело, которое идёт под этим номером. Список дел представлен в виде односвязного списка.
Напишите функцию solution, которая принимает на вход голову списка и номер удаляемого дела и возвращает голову обновлённого списка.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать только функцию,
которая принимает на вход голову списка и номер удаляемого элемента и возвращает голову обновленного списка.
Ниже дано описание структуры, которая задаёт вершину списка.
Внимание! Решение надо отправлять только в виде файла с расширением, которое соответствует вашему языку.
Иначе даже корректно написанное решение не пройдет тесты.

Формат ввода
Функция принимает голову списка и индекс элемента, который надо удалить (нумерация с нуля).
Список содержит не более 5000 элементов.
Python:
Если вы пишете на Python, функция должна называться solution и принимать на вход вершину node и номер удаляемого элемента.
Узел списка описывается следующим классом:

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

Формат вывода
Верните голову списка, в котором удален нужный элемент.
Примечания
Решение нужно отправлять в виде файла с расширением соответствующем вашему языку программирования.
Нужно выбирать компилятор make.
Для Java файл должен называться Solution.java
Для остальных языков программирования это имя использовать нельзя (имя solution тоже).
"""


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def solution(node, index):
    head = node
    curr = head

    if index == 0:
        return curr.next_item
    else:
        while index - 1:
            curr = curr.next_item
            index -= 1
        if curr.next_item is not None:
            curr.next_item = curr.next_item.next_item
        return head