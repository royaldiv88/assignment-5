s=[]
for n in range(0,10):
    a=int(input("Enter the number="))
    s.append(a)
print(s)
print("the positive nos. are=")
for i in s:
    if i>=0:
        print(i)
print("the negative nos. are=")
for i in s:
    if i<0:
        print(i)
print("the even nos. are=")
for i in s:
    if i%2==0:
        print(i)
print("the odd nos. are=")
for i in s:
    if i%2!=0:
        print(i)
print("To count number of occurences")
p=0
for i in s:
           p= s.count(i)
           print(f"{i}occurs {p} times")
