palindromes = []

for i in range(9999,1000,-1):
    for j in range(9999,i,-1):
        prod = i * j
        if str(prod) == str(prod)[::-1]:
            palindromes.append(prod)

print(max(palindromes))