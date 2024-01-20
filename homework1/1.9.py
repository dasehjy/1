a=input().split()
i=0
while i<int(len(a)/2):
    a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
    i+=1
print(a)
b=input().split()
for j in range(0,int(len(b)/2)):
    b[j],b[len(b)-j-1]=b[len(b)-j-1],b[j]
print(b)