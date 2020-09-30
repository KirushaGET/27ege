s=4
a=[0]*s
n=int(input())
for i in range(s):
    a[i]=int(input())
cnt=0
n29=0
for i in range(s,n):
    k=i%s
    if a[k]%29==0:
        n29+=1
    a_=int(input())
    if a_%29==0:
        cnt=cnt+i-s+1
    else:
        n29+=1
    a[k]=a_
print(cnt)
