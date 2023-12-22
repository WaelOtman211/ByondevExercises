
def CheckString(string,s):
    if len(string)==0 :
        print("string is empty")
        return False
    if(string[0]=="}" or string[0]=="]" or string[0]==")" ):
        print("Stack is empty")
        return False
    
    for i in range(0, len(string)):
      
      if (string[i]=="[" or string[i]=="(" or string[i]=="{" ) :
         s.append(string[i])
       
      else :
       temp=s.pop()
       if temp=="{":
           if string[i]!="}":
               return False
       elif temp=="(":
           if string[i]!=")":
               return False
       else :
           if string[i]!="]":
               return False
    if  s:
        return False          
    return True

  
def main():
    
   string= "()()((" 
   s = []
   print(CheckString(string,s))
   

if __name__ == "__main__":
    main()
     
     
     