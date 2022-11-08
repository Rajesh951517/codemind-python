n=int(input())
s=n*n
c=0
while s:
    r=s%10
    c+=r
    s=s//10
if c==n:
    print("Neon Number")
else:
    print("Not Neon Number")