"""
Гоша решил реализовать структуру данных Дек, максимальный размер которого определяется заданным числом.
Методы push_back, push_front, pop_front, pop_back работали корректно.
Но, если в деке было много элементов, программа работала очень долго.
Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию.

Формат ввода
В первой строке записано количество команд n - целое число, не превосходящее 5000.
Во второй строке записано число m - максимальный размер дека. Он не превосходит 1000.
В следующих n строках записана одна из команд:
push_back value
push_front value
pop_front
pop_back
value - целое число, по модулю не превосходящее 1000.

Формат вывода
При вызове команд pop_front и pop_back нужно вывести возвращаемое значение.
Если они вызываются для пустого дека — напечатайте 'error'.
Если команда push_back или push_front вызывается для дека, размер которого равен максимально возможному, тоже нужно вывести 'error'.

Примечания
При реализации нельзя использовать связный список.
"""
from collections import deque


class Deque:
    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0
        self.dequeue = deque()

    def push_back(self, value):
        if self.current_size == self.max_size:
            print('error')
            return None

        self.current_size += 1
        self.dequeue.append(value)

    def push_front(self, value):
        if self.current_size == self.max_size:
            print('error')
            return None

        self.current_size += 1
        self.dequeue.appendleft(value)

    def pop_front(self):
        if self.current_size == 0:
            print('error')
            return None

        elem = self.dequeue.popleft()
        print(elem)
        self.current_size -= 1

    def pop_back(self):
        if self.current_size == 0:
            print('error')
            return None

        elem = self.dequeue.pop()
        print(elem)
        self.current_size -= 1


n = int(input())
deque_max_size = int(input())

deque_instance = Deque(deque_max_size)

for i in range(n):
    inp = input()

    if inp.startswith('push'):
        command, value = inp.split()
        if command == 'push_back':
            deque_instance.push_back(value)
        elif command == 'push_front':
            deque_instance.push_front(value)

    if inp == 'pop_back':
        deque_instance.pop_back()
    if inp == 'pop_front':
        deque_instance.pop_front()
