num=int(input("enter the number:"))
array=[]
for i in range(num):
    m=int(input())
    array.append(m)
for i in range(num):
    max=array[0]
    if(max<array[i]):
        max=array[i]
print(max)
