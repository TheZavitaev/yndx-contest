# 35079268
def radix_sort(arr):
    radix = 10
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
        max_length = True
        buckets = [list() for _ in range(radix)]
        for i in arr:
            tmp = i // placement
            buckets[tmp % radix].append(i)
            if max_length and tmp > 0:
                max_length = False

        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1
        placement *= radix
    return arr


if __name__ == '__main__':
    n = input()
    n = int(n)
    inp = input()
    array = list(map(int, inp.split()))
    answer = radix_sort(array)
    print(*answer)
