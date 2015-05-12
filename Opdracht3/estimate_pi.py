import sys
import math
import random

count = 0

def drop_needle(L) :
    x = random.random()
    a = random.vonmisesvariate(0,0)
    x1 = x + L * math.cos(a)
  
    if x1 <= 0 or x1 >= 1:
        return(True)
    else:
        return(False)

if len(sys.argv) < 3:
    print("Use: estimate_pi.py N L")
    exit()
    
if len(sys.argv) > 3:
        random.seed(int(sys.argv[3]))
        
N = int(sys.argv[1])
L = float(sys.argv[2])


if L > 1:
    print("AssertionError: L should be smaller than 1")
    exit()
    
for i in range(N):   
    count += drop_needle(L)

print(int(count), "hits in", N, "tries")
print("Pi = ", (2*L*N)/(count))