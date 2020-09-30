sum=0
n=int(input())
a=[int(input())for i in range(n)]
for i in range(n-6):
    for k in range(n-6):
        j=n-k 
        if (a[j-1]*a[i])%131==0:
            sum+=1
print(sum)
   
