def mul(a):
    result=1
    while a>0:
        result*=a
        a-=1
    return result
x=int(input())
print(mul(x))
