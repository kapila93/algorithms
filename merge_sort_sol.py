#merge sort solution

def mergeSort(some_list):
    print("Splitting ",some_list)
    if len(some_list)>1:
        mid = len(some_list)//2
        lefthalf = some_list[:mid]
        righthalf = some_list[mid:]

        print "left side"
        mergeSort(lefthalf)
        print "right side"
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                some_list[k]=lefthalf[i]
                i=i+1
            else:
                some_list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            some_list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            some_list[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",some_list)
    return some_list

alist = [4 , 2, 52, 24, 34, 12, 42, 57, 23, 135, 34, 43]
mergeSort(alist)
print(alist)