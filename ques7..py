n1=1
n2=500
count=0
for i in range(n1,n2+1):
    if i%7==0 and i%11==0:
        print(i)
        count+=1
print("the total no. of numbers=",count)
