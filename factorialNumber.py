def factorialNumber(n):
    if(n<0):
        return "the number is negative"
    if(n==0):
        return 1
    n=n*factorialNumber(n-1)
    return n


def main():
      
       
        print(factorialNumber(8))
if __name__ == "__main__":
        main() 
