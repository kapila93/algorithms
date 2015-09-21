# LINEAR SEARCH

list_of_numbers = [4, 14, 13, 28, 3, 15, 83, 23]
print list_of_numbers
search_value = 28

def linear_search(number_list, value_to_find):
	for index, value in enumerate(number_list):
		if value == value_to_find:
			return index + 1

print linear_search(list_of_numbers, search_value)

