import time
import sys
file = open("prime.dat" , "w")

N = int(sys.argv[1])
aantal = 0
Lijst = list(range(0, N+1))
start = time.time()
for i in range(2, N+1):
    if i in Lijst:
        file.write(str(i)+"\n")
        aantal = aantal + 1
        for j in range(2, int(N/i)+1):
            Lijst[i*j] = 0
    else:
        continue
file.close()
end = time.time()
print('Found ' + str(aantal) + ' Prime numbers smaller than ' + str(N) + ' in ' + str(end - start) + ' seconds.')