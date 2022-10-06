first,second=0,1
n=int(input("How Many number of elements requiredd in the series"))
z=list()
for i in range(0,n):
    if i<=1:
        print(i)
        z.append(i)      
    else:
        result=second+first
        first=second
        second=result
        print(result)
        z.append(result)
print(z)
    