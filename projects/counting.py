for number in range(1,11):
    if number % 2 >= 1:
        print(number)


def reverse_list(items):
    # Build a new list by walking the original from the last index down to 0
    reversed_items = []
    for i in range(len(items) - 1, -1, -1):
        reversed_items.append(items[i])
    return reversed_items


print(reverse_list([1, 2, 3, 4, 5]))