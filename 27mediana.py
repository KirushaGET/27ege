n=int(input())
k=[0]*100
for i in range (n):
    x=int(input())
    k[x]+=1
m=0
m_sum=k[m]
while m_sum<(n//2)+1:
    m+=1
    m_sum+=k[m]
print(m)
