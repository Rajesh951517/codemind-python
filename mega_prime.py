def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def op(n):
    while n:
        r=n%10
        n=n//10
    if prime(r)==True:
        return True
    else:
        return False
k=int(input())
if prime(k)==True and op(k)==True:
    print('Mega Prime')
else:
    print('Not Mega Prime')