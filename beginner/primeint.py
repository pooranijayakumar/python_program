num1=int(input("enter two number:"))
num2=int(input())
for i in range(num1+1,num2):
    for a in range(1,1000):
        if(a%2==0):
           print(i)
           break
