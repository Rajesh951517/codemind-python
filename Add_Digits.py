def add(x):
    c=0
    while x:
        r=x%10
        c+=r
        x=x//10
    if c>9:
        return add(c)
    else:
        return c
n=int(input())
print(add(n))
        