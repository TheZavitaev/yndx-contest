# 34971573


def solution(value):
    lst = value
    lst.sort()
    cnt = 0
    while True:

        if lst[0] <= 0:
            lst.pop(0)
        if lst[0] <= 0:
            lst.pop(0)

        if len(lst) <= 1:
            break

        if lst[-1] <= 0:
            lst.pop()

        lst[-1] -= 1
        cnt += 1
        lst[0] -= 1
        lst.sort()

    return cnt


if __name__ == '__main__':
    n = input()
    inp = input()
    size_datacenter = list(map(int, inp.split()))
    answer = solution(size_datacenter)
    print(answer)
