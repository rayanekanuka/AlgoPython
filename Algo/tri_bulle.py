list_size = [3, 9, 7, 1, 6, 2, 8, 4]

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]
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