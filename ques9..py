def counter(a,i):
    n=0
    n=a.count(i)
    return n
a=[]
x=int(input("enter no. of words to be entered in list="))
for i in range(0,x):
    y=input("enter word=")
    a.append(y)
print(a)
for i in a:
  print(f"{i} occurs {counter(a,i)} times")
