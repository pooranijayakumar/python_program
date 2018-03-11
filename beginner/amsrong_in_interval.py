a=int(input("enter the two intervals:"))
b=int(input())
for i in range(a,b+1):
    temp=i
    c=0
    while(temp>0):
        num=temp%10
        c=c+num**3
        temp=temp//10
    if(c==i):
        print(c)
