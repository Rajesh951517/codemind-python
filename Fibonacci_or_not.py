n=int(input())
a=0
b=1
c=[]
for i in range(n):
    temp=a
    c.append(a)
    a=b
    b=temp+a
if n in c:
    print('True')
else:
    print('False')