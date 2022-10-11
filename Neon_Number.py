n=int(input())
k=n*n
c=0
while k>0:
    r=k%10
    c+=r
    k=k//10
if c==n:
    print('Neon Number')
else:
    print('Not Neon Number')