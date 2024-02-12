list_size = [3, 9, 7, 1, 6, 2, 8, 4]


def swap(list, i, j):
    list[i], list[j] = list[j], list[i]


def tri_insertion(list):
    print("tri_insertion\n", list)
    for i in range(1, len(list)):
        temp = list[i]
        j = i
        while j > 0 and list[j - 1] > temp:
            list[j] = list[j - 1]
            j = j - 1
        list[j] = temp
    return list


print(tri_insertion(list_size))
