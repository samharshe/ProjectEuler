def sum(n, p):
    return n*int(p/n)*(int(p/n)+1)/2

print(sum(3, 999) + sum(5, 999) - sum(15, 999))