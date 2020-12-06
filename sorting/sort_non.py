def selection(lst):
    for i in range(len(lst) - 1, -1, -1):
        c_j = 0
        c_max = 0
        for j in range(i + 1):
            if lst[j] > c_max:
                c_max = lst[j]
                c_j = j
        lst[c_j], lst[i] = lst[i], lst[c_j]
    return lst

def insertion(lst):
    sorted_lst = []
    for i in range(len(lst)):
        p = lst.pop(0)
        sorted_lst.append(p)
        for j in range(len(sorted_lst) - 1, 1, -1):
            if sorted_lst[j] < sorted_lst[j - 1]:
                sorted_lst[j], sorted_lst[j - 1] = sorted_lst[j - 1], sorted_lst[j]
    return sorted_lst

def shell(lst, increments):
    sorted_lst = []
    cur_inc = 0
    for i in range(len(lst)):
        p = lst.pop(0)
        sorted_lst.append(p)
        for j in range(len(sorted_lst) - 1, 1, -increments[cur_inc]):
            if sorted_lst[j] < sorted_lst[j - 1]:
                sorted_lst[j], sorted_lst[j - 1] = sorted_lst[j - 1], sorted_lst[j]
        if cur_inc < len(increments) - 1:
         cur_inc += 1
    return sorted_lst

def bubble(lst):
    for last in range(len(lst) -1, -1, -1):
        swapped = False
        for i in range(1, last):
            if lst[i] > lst[i + 1]:
                swapped = True
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        if not swapped:
            return lst


# MergeSort(arr[], l,  r)
# If r > l
#      1. Find the middle point to divide the array into two halves:  
#              middle m = (l+r)/2
#      2. Call mergeSort for first half:   
#              Call mergeSort(arr, l, m)
#      3. Call mergeSort for second half:
#              Call mergeSort(arr, m+1, r)
#      4. Merge the two halves sorted in step 2 and 3:
#              Call merge(arr, l, m, r)
def merge(li):
    if len(li) > 1:
        m = len(li) // 2
        r = merge(li[:m])
        l = merge(li[m:])

        lst = []
        while len(lst) < len(li):
            rP = r[0] if len(r) > 0 else None
            lP = l[0] if len(l) > 0 else None
            if lP == None:
                lst.append(r.pop(0))
            elif rP == None:
                lst.append(l.pop(0))
            elif rP > lP:
                lst.append(l.pop(0))
            else:
                lst.append(r.pop(0))
        return lst
    else:
        return li

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
# def partition(arr,low,high): 
# 	i = low		 # index of smaller element 
# 	pivot = arr[high]	 # pivot 

# 	for j in range(low , high): 

# 		# If current element is smaller than the pivot 
# 		if arr[j] < pivot: 
		
# 			# increment index of smaller element 
# 			arr[i],arr[j] = arr[j],arr[i]
# 			i = i + 1

# 	arr[i],arr[high] = arr[high],arr[i] 
# 	return i

# # The main function that implements QuickSort 
# # arr[] --> Array to be sorted, 
# # low --> Starting index, 
# # high --> Ending index 

# # Function to do Quick sort 
# def quickSort(arr,low,high): 
# 	if low < high: 

# 		# pi is partitioning index, arr[p] is now 
# 		# at right place 
# 		pi = partition(arr,low,high) 

# 		# Separately sort elements before 
# 		# partition and after partition 
# 		quickSort(arr, low, pi-1) 
# 		quickSort(arr, pi+1, high) 


def quick(items, low, high):
    if low < high:
        pi = low
        pivot = items[high]

        for j in range(low, high):
            if items[j] < pivot:
                items[pi], items[j] = items[j], items[pi]
                pi += 1

        items[pi], items[high] = items[high], items[pi]

        quick(items, low, pi - 1)
        quick(items, pi + 1, high)

        

if __name__ == '__main__':
    print(selection([1, 6, 99, 2, 3]))
    # print(insertion([1, 6, 99, 2, 3]))
    # print(bubble([1, 6, 99, 2, 3]))
    # print(merge([1, 6, 99, 2, 3, 6, 4]))
    # print(shell([1, 6, 99, 2, 3], [5, 3, 1]))
    # items = [10, 7, 8, 9, 1, 5]
    # quick(items, 0, len(items) - 1)
    # print(items)

