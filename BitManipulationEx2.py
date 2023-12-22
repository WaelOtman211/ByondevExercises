def SetBits(Number):
    if(Number==0):
        return 0 
    count=0
    mask=1
    temp=Number
    while temp!=0:
          
          if mask & temp == 1:
              count=count+1
          temp=temp >> 1    
    return count  

def main():
    num = 32
    print(SetBits(num))

if __name__ == "__main__":
    main()
