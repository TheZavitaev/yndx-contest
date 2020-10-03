# 35090599
from functools import cmp_to_key

if __name__ == '__main__':
    n = input()
    inp = input()
    lst = list(map(int, inp.split()))
    lst.sort(key=cmp_to_key(lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1))
    answer = ''.join(map(str, lst))
    print(answer)
