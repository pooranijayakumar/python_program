print("enter two numbers:")
a=int(input())
b=int(input())
c=[]
sum=0
for i in range(a):
    m=int(input())
    c.append(m)
print(c)
for i in range(b):
    sum=sum+c[i]
print(sum)    
