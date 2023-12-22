def mergeSort(array):
    if len(array)==1:
        return array
    Array1=array[0:int(len(array)/2)]
    Array2=array[int(len(array)/2):]
    
    Array1=mergeSort(Array1)
    Array2=mergeSort(Array2)
    
    return merge(Array1,Array2)

def merge(arr1,arr2):
    
    arr3=[]
    
    while len(arr1)!=0 and len(arr2)!=0 :
        if arr1[0]>arr2[0]:
            arr3.append(arr2[0])
            arr2.remove(arr2[0])
            
        else:
            arr3.append(arr1[0])
            arr1.remove(arr1[0])
    while len(arr1)!=0 :
        arr3.append(arr1[0])
        arr1.remove(arr1[0])        
    while len(arr2)!=0 :
        arr3.append(arr2[0])
        arr2.remove(arr2[0])
    
    return arr3    
    
def main():
  
    array=[2,8,5,3,9,4,1,-1,20]
    print(mergeSort(array))
if __name__ == "__main__":
    main()     