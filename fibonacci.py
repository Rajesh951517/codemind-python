n=int(input())
a=0
b=1
for i in range(n):
    temp=a
    print(a,end=' ')
    a=b
    b=temp+a