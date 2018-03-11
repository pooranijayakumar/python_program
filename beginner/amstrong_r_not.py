a=int(input("enter the number:"))
temp=a
i=0
while temp>0:
    num=temp%10
    i=i+num**3
    temp=temp//10
if(i==a):
    print("Yes")
else:
    print("No")
   
