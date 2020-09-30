m=80
b=100
a0=[0]*m
a1=[0]*m
n=int(input())
for i in range(n):
    x=int(input())
    k=x%m
    if x<=b:
        a0[k]+=1
    else:
        a1[k]+=1
s=0
for k in range(m):
    s=s+(((a1[k]*(a1[k]-1))//2)+(a0[k]*a1[k])
print(s)
