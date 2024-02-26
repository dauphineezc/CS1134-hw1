# 3a

def sum_of_squares(n):
    sum = 0
    for int in range(0, n):
        sum += (int**2)
    return sum


# 3b

n = int(input("enter a positive integer: "))
print(sum([i**2 for i in range(0, n)]))


# 3c

def sum_of_squares_of_odd(n):
    sum = 0
    for int in range(0, n):
        if int % 2 != 0:
            sum += (int**2)
    return sum


# 3d

n = int(input("enter a positive integer: "))
print(sum([i**2 for i in range(0, n) if i % 2 != 0]))
