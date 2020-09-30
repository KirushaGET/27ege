aMax = 10000
s=0
d_min=aMax+1
n=int(input())
for i in range(n):
    a=int(input())
    b=int(input())  
    c=int(input())
    if a>b:
        tmp=a
        a=b
        b=tmp
    if b>c:
        tmp=b
        b=c
        c=tmp
    if a>b:
        tmp=a
        a=b
        b=tmp
    s+=a
    if((b-a)%2>0) and ((b-a)<d_min):
        d_min=b-a
    if((c-a)%2>0) and ((c-a)<d_min):
        d_min=c-a
if s %2 !=0:
    if d_min>aMax:
        s=0
    else:
        s+=d_min
print(s)
