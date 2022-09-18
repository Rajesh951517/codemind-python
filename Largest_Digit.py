a=int(input())
b=0
while a>0:
    d=a%10
    if b<d:
        b=d
    a=a//10
print(b)

