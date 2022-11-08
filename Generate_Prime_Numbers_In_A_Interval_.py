def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
x=int(input())
y=int(input())
for j in range(x,y):
    if prime(j)==True:
        print(j)