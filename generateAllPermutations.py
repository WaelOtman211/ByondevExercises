
def permute(a, l, r): 
    if l == r: 
        print(a) 
    else: 
        for i in range(l, r): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]  # backtrack     
 
def main():
      
        a=list("abc")
        print(permute(a,0,3))
if __name__ == "__main__":
        main()