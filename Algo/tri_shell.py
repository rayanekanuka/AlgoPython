list = [3, 9, 7, 1, 6, 2, 8, 4]

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]
def tri_shell(list):
    print("\ntri_shell\n", list)
    length = len(list)
    espacements = []
    e = 0
    while e < length:
        e = (3 * e + 1)
        espacements.insert(0,e)

    print(espacements)

    for e in espacements:
        for i in range(e, length):
                temp = list[i]
                j = i
                while (j > e - 1) and (list[j - e] > temp):
                    list[j] = list[j - e]
                    j = j - e
                list[j] = temp
    return list

print(tri_shell(list))