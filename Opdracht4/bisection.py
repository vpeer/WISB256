import math
def findRoot(f,a,b,epsilon):
    m=(a+b)/2
    if f(a)==0:
        return a
    if f(b)==0:
        return b
    if f(m)==0:
        return m
    if abs(b-a)<= epsilon:
        return m
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