import numpy as np

all_prime_factors = []

def prime_factor(x):
    prime_factors = []
    for i in range(2, round(x / 2)+1):
        while(x % i == 0):
            prime_factors.append(i)
            x/=i
    if len(prime_factors) == 0:
        prime_factors.append(x)
    return prime_factors

def count(target, array):
    count = 0
    for element in array:
        if target == element:
            count+=1
    return count

def product(array):
    product = 1
    for element in array:
        product *= element
    return product

for i in range(20,1,-1):
    prime_factor_array = prime_factor(i)
    for element in prime_factor_array:
        num_missing = count(element, prime_factor_array) > count(element, all_prime_factors)
        if num_missing > 0:
            for j in range(num_missing):
                all_prime_factors.append(element)

print(product(all_prime_factors))
