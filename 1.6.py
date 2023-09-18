w,x,y,z=input().split()
a=[w,x,y,z]
for i in range(1,len(a)):
    for j in range(0,len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

print(a[0],a[1],a[2],a[3])
