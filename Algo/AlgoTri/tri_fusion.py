list = [3, 9, 7, 1, 6, 2, 8, 4]

def tri_merge(list, aff=False):
    if aff:
        print("tri_merge", list)
    if len(list) > 1:
        half_list = len(list) // 2
        list_begin = list[0: half_list]
        list_end = list[half_list: len(list)]
        tri_merge(list_begin)
        tri_merge(list_end)
        i = j = k = 0
        while i < len(list_begin) and j < len(list_end):
            if list_begin[i] < list_end[j]:
                list[k] = list_begin[i]
                i += 1
            else:
                list[k] = list_end[j]
                j += 1
            k += 1
        while i < len(list_begin):
            list[k] = list_begin[i]
            i += 1
            k += 1
        while j < len(list_end):
            list[k] = list_end[j]
            j += 1
            k += 1
    return list

print(tri_merge(list))