n=int(input("the number of rows to be printed="))
count=0
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+count),end=" ")
        count+=1
    print("")
