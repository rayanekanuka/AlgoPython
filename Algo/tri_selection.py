list_size = [3, 9, 7, 1, 6, 2, 8, 4]

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

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