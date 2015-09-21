# MERGE SORT

list_of_numbers = [4 , 2, 52, 24, 34, 12, 42, 57, 23, 135, 34, 43]
print list_of_numbers


def split_sort(some_list):
	length_of_list = len(some_list)
	left_of_list = []
	right_of_list = []
	initial = 0
	end_of_left = (length_of_list - (length_of_list / 2)) - 1
	start_of_right = end_of_left + 1
	end_of_right = length_of_list - 1

	left_list = []
	right_list = []

	for index in range(initial, end_of_left):
		left_list.append(some_list[index])

def split_list(some_list):
	half_list_length = len(some_list) / 2
	left_list = []
	
	for index in range(0, half_list_length):
		left_list.append(some_list[index])
		index += 1

def merge_sort(some_list):
	length_of_list = len(some_list)
	left_of_list = []
	right_of_list = []
	left_length = length_of_list / 2
	print left_length
	for i in range(0, left_length):
		left_of_list.append(some_list[i])
		i = i + 1
	print left_of_list

	right_length = length_of_list - left_length
	print right_length
	for j in range(right_length, length_of_list):
		right_of_list.append(some_list[j])
		j = j + 1
	print right_of_list
	print right_of_list[0]

	m = 0
	n = 0
	for k in range(0, length_of_list - 1):
		print k
		print "ok"
		if left_of_list[m] <= right_of_list[n]:
			some_list[k] = left_of_list[m]
			m = m + 1
		else:
			some_list[k] = right_of_list[n]
			n = n + 1
		print some_list
		k = k + 1
	return some_list
		
		
			
merge_sort(list_of_numbers)
