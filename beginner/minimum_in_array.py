a=int(input())
b=[]
for i in range(a):
  c=int(input())
  b.append(c)
  min=a[0]
for i in range(a):
  if(min>a[i]):
    min=a[i]
print(min)
