# doing the algebra 
def sum_squares(x):
    return ((2*(x**3)+3*(x**2)+x)/6)

def square_sums(x):
    return ((x/2)*(x+1))**2

def diff(x):
    return square_sums(x) - sum_squares(x)

print(diff(100))