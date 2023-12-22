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
     
    def search(self, val):
         if val== self.data:
             return self
         elif val > self.data:
             if self.rightChild == None:
                 return None
             found=self.rightChild.search(val)
         else :
             if self.leftChild == None:
                 return None
             found=self.leftChild.search(val)
             
         return found    
             
            
    def delete(self, val):
        if val < self.data:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(val)
        elif val > self.data:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(val)
        else:
            # Node with only one child or no child
            if self.leftChild is None:
                return self.rightChild
            elif self.rightChild is None:
                return self.leftChild

            # Node with two children
            self.data = self.rightChild.find_min_value()
            self.rightChild = self.rightChild.delete(self.data)

        return self        
            
    def find_min_value(self):
        current = self
        while current.leftChild:
            current = current.leftChild
        return current.data  
    
    
    
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
    # Searching for a value
    val=root.search(11)
    if  val== None:
        print("the val is not found  ")
    else :
        print("the val is found  " + str(val.data))
     # Deleting a value
    root.delete(11)

    # Printing BST after deletion
    print("\nBST after deletion:")
    root.PrintTree()
if __name__ == "__main__":
    main()        