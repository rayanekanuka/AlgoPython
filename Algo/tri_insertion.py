list = [3, 9, 7, 1, 6, 2, 8, 4]

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]


def tri_insertion(list):
    print("\ntri_insertion\n",  "liste : ", list)
    for i in range(1, len(list)):
        temp = list[i]
        j = i
        while j > 0 and list[j - 1] > temp:
            list[j] = list[j - 1]
            j = j - 1
        list[j] = temp
    return list


print("résultat : ",tri_insertion(list))
