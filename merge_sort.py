# Merge Sort

def mergeSort(A):
	A_len = len(A)
	if A_len > 1:
		mid = A_len / 2
		left_list = A[:mid]
		right_list = A[mid:]
		mergeSort(left_list)
		mergeSort(right_list)
		i = 0
		j = 0
		k = 0
		while i < len(left_list) and j < len(right_list):
			if left_list[i] <= right_list[j]:
				A[k] = left_list[i]
				i = i + 1
			else:
				A[k] = right_list[j]
				j = j + 1
			k = k + 1

		while i < len(left_list):
			A[k]=left_list[i]
			i=i+1
			k=k+1

		while j < len(right_list):
			A[k]=right_list[j]
			j=j+1
			k=k+1
		return A
		

list_of_numbers = [4 , 2, 52, 24, 34, 12, 42, 57, 23, 135, 34, 43]
print " ^_^ "
print list_of_numbers

mergeSort(list_of_numbers)

print list_of_numbers
print " ^_^ "

