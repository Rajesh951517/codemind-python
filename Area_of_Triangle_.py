import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
s=s*(s-a)*(s-b)*(s-c)
area=math.sqrt(s)
print('{:.2f}'.format(area))