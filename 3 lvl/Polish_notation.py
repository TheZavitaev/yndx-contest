# 34796867
"""
Задание связано с обратной польской нотацией.
Она используется для парсинга арифметических выражений.
По сравнению с другим приемом, применяемым для данной задачи —
использованием дерева операций,
она является более компактной, так как в ней не используются скобки.
Еще её иногда называют обратной польской записью или постфиксной нотацией.

В постфиксной нотации операнды расположены перед знаками операций.

Пример 1:
3 4 +
будет равно 7, и означает 3 + 4

Пример 2:
10 2 4 * -
будет равно 2, и означает 10 - 2 * 4

Разберем последний пример подробнее:

Знак * стоит сразу после чисел 2 и 4, значит к ним нужно применить операцию,
которую этот знак обозначает, то есть перемножить эти два числа.
В результате получим 8

После этого выражение приобретет вид:

10 8 -

Операцию минус нужно применить к двум идущим перед ней числам, то есть 10 и 8.
В итоге получаем 2.

Рассмотрим алгоритм более подробно. Для его реализации будем использовать стек.

Для вычисления значения выражения, записанного в обратной польской нотации,
нужно считывать выражение слева направо и придерживаться следующих шагов:

1. Обработка входного символа: - Если на вход подан операнд,
он помещается на вершину стека.
- Если на вход подан знак операции, она выполняется над требуемым количеством
значений из стека, взятых в порядке добавления.
Результат выполненной операции помещается на вершину стека.
2. Если входной набор символов обработан не полностью, перейти к шагу 1.
3. После полной обработки входного набора символов результат вычисления
выражения находится в вершине стека.

Формат ввода
В единственной строке дано выражение, записанное в обратной польской нотации.
Числа и арифметические операции отделены друг от друга пробелами.

На вход могут подаваться операции: +, -, *, / и числа,
по модулю не превосходящие 10000.

Гарантируется, что значение промежуточных выражений в тестовых данных
по модулю не больше 50000.

Формат вывода
Единственное число - значение выражения.

Пример 1
Ввод
2 1 + 3 *

Вывод
9

Пример 2
Ввод
7 2 + 4 * 2 +

Вывод
38
"""
import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[len(self.items) - 1]


def reversed_polish_notation(expr):
    stack = Stack()
    for _ in expr:

        try:
            oper = int(_)
            stack.push(oper)
        except ValueError:
            cnt1, cnt2 = stack.pop(), stack.pop()
            stack.push(OPERATORS[_](cnt2, cnt1))

    return stack.pop()


if __name__ == '__main__':
    inp = input()
    expr = inp.split()
    answer = int(reversed_polish_notation(expr))
    print(answer)
