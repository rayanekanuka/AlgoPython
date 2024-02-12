list = [3, 9, 7, 1, 6, 2, 8, 4]

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]
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

print(tri_shell(list))