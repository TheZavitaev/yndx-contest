# 35074960

def binary_search(lst, k):
    first = lst[0]
    low = 0
    hight = len(lst) - 1
    search_index = int(k)

    while low <= hight:
        mid = int(low + (hight - low) / 2)
        if search_index == lst[mid]:
            return mid

        if (lst[mid] < first) != (search_index < first) or (lst[mid]
                                                            < search_index):
            low = mid + 1
        else:
            hight = mid - 1
    return -1


len_arr = input()
k = input()  # Искомый эллемент
inp = input()
broken_array = list(map(int, inp.split()))
answer = binary_search(broken_array, k)
print(answer)
