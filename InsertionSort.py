def find_place(list2,number):
	if len(list2) == 1:
		if list2[0] < number:
			return 1
	if len(list2) > 0 and number <= list2[0]:
		return 0
	start = 0
	end = len(list2)
	while end - start > 1:
		midpoint = (end + start) // 2
		if list2[midpoint] > number:
			end = midpoint
		elif list2[midpoint] < number:
			start = midpoint
		else:
			return midpoint
	return end
 
 def insertsort(list_in):
  list_out = [list_in[0]]
  for element in list_in[1,-1]:
    list_out.insert(find_place(list_out,element),element)
  return list_out
