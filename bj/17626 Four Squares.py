import sys,math

def ss(n,c,acc):
    if n==0:
        return c
    elif n==1:
        c.append(1)
        return c
    else:
        a = math.floor(math.sqrt(n)-acc)
        if a<=0:
            c=[i for i in range(n)]
            return c
        c.append(a)
        b = n - math.pow(a, 2)
        return ss(b,c,0)

n=int(sys.stdin.readline())
c=[]
a=math.floor(math.sqrt(n))
min=50000
mm=[]

for i in range(a):
    c=ss(n,[],i)
    if len(c)<min:
        min=len(c)
        mm=c
print(min)