a=[0]*12
n=int(input())
for i in range(n):
    k=int(input())
    ost12=k%12
    a[ost12]+=1
    #print(a)
s=0
for i in range(1,6):
    s+=a[i]*a[12-i]
s+=a[0]*(a[0]-1)//2 + a[6]*(a[6]-1)//2
print (s)
