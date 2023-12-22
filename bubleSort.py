

def BubbleSort(array):
    
    for i in range(1, len(array)):
        for j in range(0, len(array)-1):
           if array[j]>array[j+1]:
             temp=array[j]
             array[j]=array[j+1]
             array[j+1]=temp
        
    
    return array



def main():
  
    array=[2,8,5,3,9,4,1]
    print(BubbleSort(array))
if __name__ == "__main__":
    main() 