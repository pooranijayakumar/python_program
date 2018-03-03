num=int(input("enter the number:"))
for i in range(2,1001):
    if (num%i)!=0 and num%1==0:
        print("prime number")
        break
    else:
     print("not a prime number")
     break    
