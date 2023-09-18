x,y,z =input().split()
temp=0
if x<y:
    temp=x
    x=y
    y=temp
if y<z:
    temp=y
    y=z
    z=temp
if x<y:
    temp=x
    x=y
    y=temp
print(z,y,x)