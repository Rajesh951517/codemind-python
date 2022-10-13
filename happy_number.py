def happy(x):
    r=0
    while x:
        k=x%10
        r+=k*k
        x//=10
    if r<9:
        return r
    else:
        return happy(r)
n=int(input())
if happy(n)==1 or happy(n)==7:
    print('True')
else:
    print('False')
        