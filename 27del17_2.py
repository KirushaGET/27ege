sum=0
a=[]
n=int(input())
for i in range (0,n):
    a.append(int(input()))
for i in range (0,n-1):
    for k in range (i+1,n):
        if ((a[i]-a[k])%2==0) and (a[i]%17==0 or a[k]%17==0) and sum<(a[i]+a[k]):
            sum=a[i]+a[k]
            d=i
            f=k
if sum !=0:
    print(a[d],a[f])
else:
    print('00')
