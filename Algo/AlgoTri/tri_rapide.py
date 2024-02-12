list = [3, 9, 7, 1, 6, 2, 8, 4]


def swap(list, i, j):
    list[i], list[j] = list[j], list[i]


def tri_quick(list, first, last):
    if first < last:
        pivot = partition(list, first, last)
        tri_quick(list, first, pivot - 1)
        tri_quick(list, pivot + 1, last)
    return list


def partition(list, first, last):
    pivot = list[last]
    j = first
    for i in range(first, last):
        print("à chaque tour : ", list)
        if list[i] <= pivot:
            swap(list, i, j)
            j += 1
    swap(list, last, j)
    return j

print("\n résulat : ", tri_quick(list, 0, len(list) - 1))
