largest_p = 9009

for i in range(100,999):
    for j in range(100,999):
        prod = i * j
        if str(prod) == str(prod)[::-1]  and prod > largest_p:
            largest_p = prod

print(largest_p)