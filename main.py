import insertion_sort
import merge_sort
import modified_quicksort
import inplace_quicksort
import datetime
import random
 
# Code to generate random numbers and append them to a list
# start = starting range,
# end = ending range
# num = number of elements needs to be appended
def Rand(start, end, num):
    res = []
 
    for j in range(num):
        res.append(random.randint(start, end))
 
    return res

def sorting_algorithms(arrayToBeSorted):
    # Calling Insertion sort and calculating time elapsed
    print("\n\n*********INSERTION SORT**********")
    #print("\nArray Before Sort")
    arrayToBeSorted1=list(arrayToBeSorted)
    #print(arrayToBeSorted1)
    startTime1 = datetime.datetime.now()
    sorted_array= insertion_sort.insertionSort(arrayToBeSorted1)
    endTime1 = datetime.datetime.now()
    diff = endTime1 - startTime1
    timeElapsed1=diff.total_seconds() * 1000
    #print ("\n\nSorted array after Insertion sort is:")
    #print(sorted_array)
    print("\nTime elapsed in milliseconds after Insertion sort is : ")
    print(timeElapsed1)


    # Calling merge sort and calculating time elapsed
    print("\n\n\n*********MERGE SORT**********")
    #print("\nArray Before Sort")
    arrayToBeSorted2=list(arrayToBeSorted)
    #print(arrayToBeSorted2)
    n = len(arrayToBeSorted2)
    startTime2 = datetime.datetime.now()
    merge_sort.mergeSort(arrayToBeSorted2,0,n-1)
    endTime2 = datetime.datetime.now()
    diff = endTime2 - startTime2
    timeElapsed2=diff.total_seconds() * 1000
    #print ("\n\nSorted array after merge sort is")
    #print (arrayToBeSorted2)
    print("\n\nTime elapsed in milliseconds after Merge-sort is : ")
    print(timeElapsed2)

    # Calling In-place quicksort sort and calculating time elapsed
    print("\n\n\n*********IN-PLACE QUICKSORT**********")
    #print("\nArray Before Sort")
    arrayToBeSorted3=list(arrayToBeSorted)
    #print(arrayToBeSorted3)
    n = len(arrayToBeSorted3)
    startTime3 = datetime.datetime.now()
    inplace_quicksort.quickSort(arrayToBeSorted3,0,n-1)
    endTime3 = datetime.datetime.now()
    diff = endTime3 - startTime3
    timeElapsed3=diff.total_seconds() * 1000
    #print ("\n\nSorted array after In-place quicksort is:")
    #print (arrayToBeSorted3)
    #for i in range(n):
    #print ("%d" %arrayToBeSorted3[i]),
    print("\n\nTime elapsed in milliseconds after Quicksort is : ")
    print(timeElapsed3)

    # Calling Modified Quicksort and calculating time elapsed
    print("\n\n\n*********MODIFIED QUICKSORT**********")
    #print("\nArray Before Sort")
    arrayToBeSorted4=list(arrayToBeSorted)
    #print(arrayToBeSorted4)
    n = len(arrayToBeSorted4)
    startTime4 = datetime.datetime.now()
    modified_quicksort.quickSort(arrayToBeSorted4,0,n-1)
    endTime4 = datetime.datetime.now()
    diff = endTime4 - startTime4
    timeElapsed4=diff.total_seconds() * 1000
    #print ("\n\nSorted array after Modified quicksort is:")
    #print (arrayToBeSorted4)
    print("\n\nTime elapsed in milliseconds after Modified Quicksort is : ")
    print(timeElapsed4)


# Driver code to generate array list of random numbers
input_size_array =[500]
#input_size_array =[500,1000,2000,4000,5000,10000,20000,30000,40000,50000]
start = 1
end = 100000
for x in range(len(input_size_array)):
    for y in range(3):
        num = input_size_array[x]
        arrayToBeSorted= Rand(start, end, num)
        
        #Case 1: Randomized array
        sorting_algorithms(arrayToBeSorted)
        
        #Case 2:
 #       insertion_sort.insertionSort(arrayToBeSorted)
 #       temp_array = list(arrayToBeSorted_temp)
 #       n = len(temp_array)
#        modified_quicksort.quickSort(temp_array,0,n-1)
 #      sorting_algorithms(arrayToBeSorted)
     
        #Case 3:
  #      temp_array = list(arrayToBeSorted)
#        n = len(temp_array)
#        sorted_array = modified_quicksort.quickSort(temp_array,0,n-1)
#        reversed_sorted_array = list(reversed(sorted_array)
#        sorting_algorithms(reversed_sorted_array)              
 
