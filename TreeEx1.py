class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
 
    def insert(self,data):
        
        if data < self.data:
            if self.leftChild != None:
               # if we still need to move towards the left subtree
                self.leftChild.insert(data) 
            else:
             self.leftChild= Node(data)
             return
        else:
            if self.rightChild != None:
                self.rightChild.insert(data)
                
            else:
                self.rightChild=Node(data)
                return 
        
    def PrintTree(self):
         
        if self.leftChild:
            self.leftChild.PrintTree()
            
        print(self.data)
        if self.rightChild:
            self.rightChild.PrintTree()
     
    def GetThelowestAncestor(self,n1,n2):
                
        if (n1>self.data and n2<self.data) or (n1<self.data and n2>self.data) :
             
             return self.data
        elif  (n1<self.data and n2<self.data):
            
            if n1==self.leftChild.data or n2==self.leftChild.data:
                 
                return self.data
            else:
                   
                  low = self.leftChild.GetThelowestAncestor(n1, n2)
                  
        else:
            
            if n1==self.rightChild.data or n2==self.rightChild.data:
                
                return self.data
            else:
               low = self.rightChild.GetThelowestAncestor(n1, n2)
        return low
                 
            
            
            
        
def main():
    
    root = Node(27)
# Inserting values in BST
    root.insert(14)
    root.insert(35)
    root.insert(31)
    root.insert(19)
    root.insert(10)
    root.insert(11)
    root.insert(5)
    root.insert(4)
    
   
    
# printing BST
    root.PrintTree()
   
     
    print("the lowest is:"+str(root.GetThelowestAncestor(31,35)))
if __name__ == "__main__":
    main()        