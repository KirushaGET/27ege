n=int(input())
a=[int(input())for i in range(n)]
x=y=sum=0
for i in range (n):
    for j in range(i+1, n):
        if a[i]>a[j] and (a[i]+a[j])%251==0:
            if(a[i]+a[j]>sum):
                sum=a[i]+a[j]
                x=a[i]
                y=a[j]
print(x,y)
