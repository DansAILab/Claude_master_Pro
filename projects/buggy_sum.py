def sum_of_first_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print(sum_of_first_n(5))