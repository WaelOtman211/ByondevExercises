def evenOrOdd(Number):
    if(Number==0):
        return "Even Number" 
    mask = 1
    if mask & Number == 0:
        return "Even Number"
    return "Odd Number"

def main():
    num = -1
    print(evenOrOdd(num))

if __name__ == "__main__":
    main()
