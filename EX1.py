""""""""""""""""""""""""""""""
def RemoveDeplucate(arr):  
    array =[]
    array.append(arr[0])     
    for i in range(1, len(arr)):
       	if arr[i]!=arr[i-1]:
           array.append(arr[i])
    return array     
""""""""""""""""""""""""""""""
def  RevrseFunc(ReversString):
    for i in range(0, int(len(ReversString)/2)):
        temp = ReversString[i]
        ReversString = ReversString[:i] + ReversString[len(ReversString) - i - 1] + ReversString[i + 1:]
        ReversString = ReversString[:len(ReversString) - i - 1] + temp + ReversString[len(ReversString) - i - 1 + 1:]
    return ReversString    
""""""""""""""""""""""""""""""
def FindMin(arr):
    min=arr[0]
    for i in range(0, len(arr)):
        if min>arr[i]: 
            min=arr[i]
    return min

def FindMax(arr):
    max=arr[0]
    for i in range(0, len(arr)):
        if max<arr[i]: 
            max=arr[i]
    return max
""""""""""""""""""""""""""""""


def main() :
    
    ReversString="World"
    arr =[1,2,2,3,7,7,77]
    print(FindMax(arr))
    print(FindMin(arr))
    print(RemoveDeplucate(arr))
    print(RevrseFunc(ReversString))
    
if __name__ == "__main__":
    main()
     