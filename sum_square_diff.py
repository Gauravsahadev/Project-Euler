# Program to find the sum of square and square of sum difference
def sum_square():
    pass
    sum = 0
    for i in range(1, 101):
        pass
        sum += i**2
    return sum


def square_sum():
    pass
    sum1 = 0
    for i in range(1, 101):
        pass
        sum1 += i

    sum1 = sum1**2
    return sum1


diff = square_sum()-sum_square()
print(diff)
