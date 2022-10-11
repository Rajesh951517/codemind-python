n=int(input())
a=0
b=1
while n>0:
    r=n%10
    a+=r
    b=b*r
    n=n//10
if a==b:
    print('Spy Number')
else:
    print('Not Spy Number')