def insertionSort(array,low,high):
        for j in range (low+1, high+1):
            key = array[j]
            i = j-1
            while i >= 0 and array[i]>key:
                array[i+1]=array[i]
                i=i-1
            array[i+1]=key
        return array
