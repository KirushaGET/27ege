n=int(input())
k0=0
k1=0
k2=0
for i in range(n):
    ch=int(input())
    if ch%3==0:
        k0+=1
    elif ch%3==1:
        k1+=1
    else:
        k2+=1
s=0
s=k0*(k0-1)*(k0-2)//6+k1*(k1-1)*(k1-2)//6+k2*(k2-1)*(k2-2)//6+k0*k1*k2
print(s)
