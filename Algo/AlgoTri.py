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


def tri_selection(list):
    print("\ntri_selection\n", list)
    for i in range(1, len(list)):
        min_index = list[i]
        j = i
        while j > 0 and list[j - 1] < min_index:
            list[j] = list[j - 1]
            j = j - 1
        list[j] = min_index
    return list


print(tri_selection(list_size))


def tri_bulle(list):
    print("\ntri_bulle\n", list)
    passage = 0
    permut = True
    while permut:
        permut = False
        passage += 1
        for i in range(0, (len(list) - passage)):
            if list[i] > list[i + 1]:
                swap(list, i, (i + 1))
                permut = True
    return list


print(tri_bulle(list_size))


def tri_shell(list):
    print("\ntri_shell\n", list)
    e = 0
    while e < (len(list) / 3):
        e = (3 * e + 1)
    while e != 0:
        for i in range(e, len(list)):
            temp = list[i]
            j = i
            while (j > e - 1) and (list[j - e] > temp):
                list[j] = list[j - e]
                j = j - e
            list[j] = temp
        e = int(((e - 1) / 3))
    return list

print(tri_shell(list_size))