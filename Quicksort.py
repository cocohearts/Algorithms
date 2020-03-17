import random
import time

def quicksort(list_in):
    if len(list_in) == 1:
        return list_in
    pivot = list_in[0]
    smaller_list = []
    bigger_list = []
    for r in list_in[1:]:
        if r < pivot:
            smaller_list.append(r)
        else:
            bigger_list.append(r)
    if len(smaller_list) == 0:
        return [pivot] + quicksort(bigger_list)
    elif len(bigger_list) == 0:
        return quicksort(smaller_list) + [pivot]
    return quicksort(smaller_list)+[pivot]+quicksort(bigger_list)