n1=int(input("enter first number of range="))
n2=int(input("enter second number of range="))
n=n1
count=0
while(n<=n2):
   if n>1:
     for i in range(2,n):
        if n%i==0:
            break
     else:
        print(n)
        count+=1
     n+=1
