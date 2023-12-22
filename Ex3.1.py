from _collections import deque

 
class Stack:
    
    def __init__(self):
 
        # Two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x):
        
        self.q2.append(x)
        
        while self.q1 :
           self.q2.append(self.q1.popleft())
        
           
        self.q1, self.q2 = self.q2, self.q1
  
    def pop(self):
 
        # if no elements are there in q1
        if self.q1:
            self.q1.popleft()
 
    def top(self):
        if (self.q1):
            return self.q1[0]
        return None
 
    def size(self):
        return len(self.q1)
        





  
def main():
   s = Stack()
   s.push(1)
   s.push(2)
   s.push(3)

   print("current size: ", s.size())
   print(s.top())
   s.pop()
   print(s.top())
   s.pop()
   print(s.top())
if __name__ == "__main__":
    main()
     
     
     