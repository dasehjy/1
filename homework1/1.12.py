x=float(input())
e=0.0001
if x==0:
    print(0)
else:
    low=0
    high=x
    while True:
        mid=(low+high)/2
        diff=mid**3-x
        if abs(diff)<=e:
            break
        elif diff<0:
            low=mid
        else:
            high=mid
    print(mid)
   

