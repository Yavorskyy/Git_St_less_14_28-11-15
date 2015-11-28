def linear_factorial(x):
    result = 1
    for i in xrange(1, x + 1):
        result *= i
    return result

linear_factorial(500)
