#2nd question
a=int(input('enter the starting range'))
b=int(input('enter the ending range'))
c=int(input('enter the number'))
for i in range(a,b+1):
    if (i%c!=0):
        break
    else:
        print(i)
