a=[1,2,3,4,5,6,7,8,9,10]
count_odd=0
count_even=0
for x in a:
    if(x%2==0):
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print("total even numbers are:")
print(count_even)
print("total odd numbers are:")
print(count_odd)
