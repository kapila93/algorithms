# QUICK SORT

# recursively sorts the list
def quicksort(some_list, start_index, last_index):
  if start_index <= last_index:
    pivot_index = partition(some_list, start_index, last_index)
    quicksort(some_list, start_index, pivot_index - 1)
    quicksort(some_list, pivot_index + 1, last_index)

# sorts the list in relation to the pivot value, 
# returns the pivot index we use to start the sort on the next recursive call
def partition(some_list, start_index, last_index):
  pivot_index = start_index
  for index in range(start_index + 1, last_index + 1):
    if some_list[index] <= some_list[start_index]:
      pivot_index = pivot_index + 1
      some_list[index], some_list[pivot_index] = some_list[pivot_index], some_list[index]
  some_list[pivot_index], some_list[start_index] = some_list[start_index], some_list[pivot_index]
  return pivot_index

a_list = [54,26,93,17,77,31,44,55,20]
print a_list
quicksort(a_list, 0, len(a_list)-1)
print a_list






