def LinearSearch(array,val):
    
    for i in range(0, len(array)):
        if val== array[i]:
            return "value is found in index "+ str(i)
    
    return "value not found"


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    first, middle, last = arr[0], arr[len(arr)//2], arr[-1]
    pivot = sorted([first, middle, last])[1]

    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for x in arr:
        if x < pivot:
            less_than_pivot.append(x)
        elif x == pivot:
            equal_to_pivot.append(x)
        else:
            greater_than_pivot.append(x)

    sorted_less = quicksort(less_than_pivot)
    sorted_greater = quicksort(greater_than_pivot)

    return sorted_less + equal_to_pivot + sorted_greater

def BinarySearch(array, low, high, x):
 
    # Check base case
    if high >= low:
 
        middle = (high + low) // 2
 
        # If element is present at the middle itself
        if array[middle] == x:
            return "value is found in index "+ str(middle)
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif array[middle] > x:
            return BinarySearch(array, low, middle - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return BinarySearch(array, middle + 1, high, x)
 
    else:
         
        return "value not found"
    
    
     
    
    

def main():
  
    array=[2,8,5,3,9,4,1]
    print("in Linary:")
    print(LinearSearch(quicksort(array),6))
   
    print("in Binary:")
    print(BinarySearch(quicksort(array),0,6,6))
    
    print("in Linary:")
    print(LinearSearch(quicksort(array),9))
   
    print("in Binary:")
    print(BinarySearch(quicksort(array),0,6,3))
if __name__ == "__main__":
    main() 
