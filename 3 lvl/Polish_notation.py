# 34723937
import re

OPERATORS = {
    '+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__truediv__,
    '%': float.__mod__,
    '^': float.__pow__,
}


def reversed_polish_notation(expr):
    ops = OPERATORS.keys()
    stack = []

    for atom in re.split(r'\s+', expr):
        try:
            atom = float(atom)
            stack.append(atom)
        except ValueError:
            for oper in atom:
                if oper not in ops:
                    continue
                try:
                    oper2 = stack.pop()
                    oper1 = stack.pop()
                except IndexError:
                    raise Exception('Мало операндов')

                try:
                    oper = OPERATORS[oper](oper1, oper2)
                except ZeroDivisionError:
                    raise Exception('Деление на ноль')

                stack.append(oper)

    if len(stack) != 1:
        raise Exception('Много операндов')

    return stack.pop()


print(int(reversed_polish_notation(input())))
