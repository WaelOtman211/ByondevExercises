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
def main():
  
    array=[2,8,5,3,9,4,1]
    print(quicksort(array))
if __name__ == "__main__":
    main() 
