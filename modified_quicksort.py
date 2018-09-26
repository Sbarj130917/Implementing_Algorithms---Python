import datetime
import quick_insertion_sort
import pdb
import random
from numpy import median


    #length = high - low
    #length = len(arr)
    #middle = length/2
    #pivot = int(median([arr[low],arr[high],arr[middle]]))  # pivot as median of three
    #arr[high],arr[pivot

def MedianOfThree(arr, low, high):
    mid = (low + high)/2
    if arr[high] < arr[low]:
        Swap(arr, low, high)        
    if arr[mid] < arr[low]:
        Swap(arr, mid, low)
    if arr[high] < arr[mid]:
        Swap(arr, high, mid)
    Swap(arr,mid,high)
    return arr[high]


# Generic Swap for manipulating list data.
def Swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp


# array_to_be_sorted[] --> Array which is to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Partition Function
def array_partition(array_to_be_sorted,low,high):
    x = ( low-1 )         # index of smaller element
    pivot= MedianOfThree (array_to_be_sorted,low,high)
    for y in range(low , high):
 
        # If current element is smaller than or equal to pivot
        if   array_to_be_sorted[y] <= pivot:
                                                                                                                     
            # increment index of smaller element
            x = x+1
            array_to_be_sorted[x],array_to_be_sorted[y] = array_to_be_sorted[y],array_to_be_sorted[x]
 
    array_to_be_sorted[x+1],array_to_be_sorted[high] = array_to_be_sorted[high],array_to_be_sorted[x+1]
    return ( x+1 )
 
# Quick sort function
def quickSort(array_to_be_sorted,low,high):
    #pdb.set_trace()
    if (high-10) > low:
        if low < high:
 
            # pi is partitioning index
            pi = array_partition(array_to_be_sorted,low,high)
 
            # Separately sort elements before partition and after partition
            quickSort(array_to_be_sorted, low, pi-1)
            quickSort(array_to_be_sorted, pi+1, high)
    else:
        quick_insertion_sort.insertionSort(array_to_be_sorted,low,high)

