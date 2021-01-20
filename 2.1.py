fibs = [1,1]
while(fibs[-1]+fibs[-2]<4000000):
    fibs.append(fibs[-1]+fibs[-2])

print(sum(fib for fib in fibs if fib % 2 == 0))