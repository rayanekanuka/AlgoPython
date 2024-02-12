list = [3, 9, 7, 1, 6, 2, 8, 4]

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def tri_selection(list):
    print("\ntri_selection\n", "liste : ", list)
    length = len(list)
    for i in range(0, length):
        min = i
        for j in range(i+1, length):
            if list[j] < list[min]:
                min = j
        swap(list, i, min)
        print("chaque tour de boucle :", list)
    return list


print("résultat : ",tri_selection(list))