# array_to_be_sorted[] = Array which is to be sorted,
# low  = Starting index of the array,
# high = Ending index of the array

def array_partition(array_to_be_sorted,low,high):
    pivot = array_to_be_sorted[high]     # last element of the array is being taken as pivot
    x = ( low-1 )
    
    for y in range(low , high):
        # check whether current element is smaller than or equal to pivot
        if   array_to_be_sorted[y] <= pivot:
            # increment index of smaller element
            x = x+1
            array_to_be_sorted[x],array_to_be_sorted[y] = array_to_be_sorted[y],array_to_be_sorted[x]
    array_to_be_sorted[x+1],array_to_be_sorted[high] = array_to_be_sorted[high],array_to_be_sorted[x+1]
    return ( x+1 )


# Quick sort function
def quickSort(array_to_be_sorted,low,high):
    if low < high:
        # pi is partitioning index
        pi = array_partition(array_to_be_sorted,low,high)
        
        # Sorting of elements separately before and after partition
        quickSort(array_to_be_sorted, low, pi-1)
        quickSort(array_to_be_sorted, pi+1, high)


