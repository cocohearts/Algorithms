def stringify(list_in):
    list_out = []
    for r in list_in:
        list_out.append(str(r))
    return list_out

def intify(list_in):
    list_out = []
    for r in list_in:
        list_out.append(int(r))
    return list_out

def nth_last_digit(n,integer):
    if len(str(integer))<n:
        return 0
    return int(str(integer)[-n])
def extract_digit(list_in,n_digit):
    counter_list = []
    for r in range(10):
        counter_list.append([])
    for number in list_in:
        counter_list[nth_last_digit(n_digit,number)].append(number)
    list_out = []
    for minilist in counter_list:
        list_out += minilist
    return list_out
def radixsort(unsorted_list):
    for r in unsorted_list:
        if len(str(r)) > max_len:
            max_len = len(str(r))
    for digit in range(1,max_len+1):
        sorted_list = extract_digit(sorted_list,digit)
    return(sorted_list)
