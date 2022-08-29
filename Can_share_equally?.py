a,b=map(int,input().split())
c=a+(b*2)
if a==0:
    if b%2==0:
        print("YES")
    else:
        print("NO")
else:
    if c%2==0:
        print("YES")
    else:
        print("NO")