num1=int(input("enter two number:"))
num2=int(input())
for i in range(num1,num2+1):
  if(i>1):
    for a in range(2,i):
      if(i%a==0):
        break
      else:
        print(i)
        break
