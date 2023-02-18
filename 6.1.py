def sum_squares(x):
    sum = 0
    for i in range(x+1):
        print(i**2)
        sum += i**2
    print(sum) 
    return sum

def square_sums(x):
    return ((x/2)*(x+1))**2

def diff(x):
    return square_sums(x) - sum_squares(x)

print(diff(100))