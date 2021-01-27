def lpf(n):
    last_factor = 1
    if(n%2==0):
        n/=2
        last_factor = 2
        while(n%2==0):
            n/=2
    max_factor = n**0.5
    factor = 3
    while(n > 1 and factor <= max_factor):
        if(n % factor == 0):
            n/=factor
            last_factor = factor
            while n % factor == 0:
                n/=factor
            max_factor = n**0.5
        factor+=1
    if n == 1:
        return last_factor
    return n

print(lpf(600851475143))