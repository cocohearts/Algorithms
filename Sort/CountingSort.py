def counting_sort(list_in):
    counting_list = []
    for r in range(max(list_in) + 1):
        counting_list.append(0)

    for r in list_in:
        counting_list[r] += 1

    sorted_list = []
    for r in range(len(counting_list)):
        for s in range(counting_list[r]):
            sorted_list.append(r)
    return sorted_list
