"""
На вход подается строка. Нужно определить длину наибольшей подстроки,
которая не содержит повторяющиеся символы.

Формат ввода
Одна строка, состоящая из латинских букв. Длина строки не превосходит 10000.

Формат вывода
Одно число - ответ на задачу.
"""

substr = str(input())


def findLongest(s):
    maxlen = 0
    longest = ""
    for i in range(0, len(s)):
        subs = s[i:]
        chars = set()
        for j, c in enumerate(subs):
            if c in chars:
                break
            else:
                chars.add(c)
        else:
            j += 1

        if j > maxlen:
            maxlen = j
            longest = s[i:i + j]
    return longest


print(len(findLongest(substr)))
