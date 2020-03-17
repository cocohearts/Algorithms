def merge_sort(list2):
	if len(list2) == 1:
		return list2
	midpoint = len(list2) // 2
	sorted_list_1half = merge_sort(list2[0:midpoint])
	sorted_list_2half = merge_sort(list2[midpoint:])
	sorted_list = []
	while not ((len(sorted_list_1half) == 0) or (len(sorted_list_2half) == 0)):
		if sorted_list_1half[0]>sorted_list_2half[0]:
			sorted_list.append(sorted_list_2half[0])
			del sorted_list_2half[0]
		else:
			sorted_list.append(sorted_list_1half[0])
			del sorted_list_1half[0]
	sorted_list.extend(sorted_list_1half)
	sorted_list.extend(sorted_list_2half)
	return sorted_list
