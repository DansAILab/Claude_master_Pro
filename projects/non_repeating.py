def first_non_repeating(text):
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] = char_counts[char] + 1
        else:
            char_counts[char] = 1

    for char in text:
        if char_counts[char] == 1:
            return char

    return None

print(first_non_repeating("swiss"))