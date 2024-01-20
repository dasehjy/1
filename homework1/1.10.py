a=input()
flag=0
for i in range(0,len(a)-1):
    if a[i]==a[i+1]:
        print("有连续相同字符")
        flag=1
        break
if flag==0:
    print("没有连续相同字符")