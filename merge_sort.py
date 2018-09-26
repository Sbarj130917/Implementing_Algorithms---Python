def merge(array_to_be_sorted, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
 
    # creation of temporary arrays for merging
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for x in range(0 , n1):
        L[x] = array_to_be_sorted[left + x]
 
    for y in range(0 , n2):
        R[y] = array_to_be_sorted[mid + 1 + y]
 
    # Merge the temp arrays back into array_to_be_sorted[left..right]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = left  # Initial index of merged subarray
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            array_to_be_sorted[k] = L[i]
            i += 1
        else:
            array_to_be_sorted[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there are any items remaining
    while i < n1:
        array_to_be_sorted[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there are any items remaining
    while j < n2:
        array_to_be_sorted[k] = R[j]
        j += 1
        k += 1
 


def mergeSort(array_to_be_sorted,left,right):
    if left < right:

        #find the middle index of the array
        mid = (left+right)/2
 
        #Recursively calling mergesort to sort first and second half of the array
        mergeSort(array_to_be_sorted, left, mid)
        mergeSort(array_to_be_sorted, mid+1, right)
        merge(array_to_be_sorted, left, mid, right)
