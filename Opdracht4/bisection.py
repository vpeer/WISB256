import math
def findRoot(f,a,b,epsilon):
    m=(a+b)/2
    if f(a)==0:
        print(a)
        exit()
    if f(b)==0:
        print(b)
        exit()
    if f(m)==0:
        print(m)
        exit()
    if abs(b-a)<= epsilon:
        print(m)
        exit()
    if f(a)<0 and f(b)>0:
        if f(m)< 0:
            return findRoot(f,m,b,epsilon)
        if f(m)>0:
            return findRoot(f,a,m,epsilon)
    if f(a)>0 and f(b)<0:
        if f(m)> 0:
            return findRoot(f,m,b,epsilon)
        if f(m)<0:
            return findRoot(f,a,m,epsilon)
    else:
        exit()