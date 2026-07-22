def most_frequent_character(text):
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] = char_counts[char] + 1
        else:
            char_counts[char] = 1

    for char in text:
        if char_counts[char] == max(char_counts.values()):
            return char

    return None

print(most_frequent_character("mississippi"))