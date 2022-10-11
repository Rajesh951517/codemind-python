def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
n=int(input())
if prime(n)==True:
    print('prime')
else:
    print('not a prime')