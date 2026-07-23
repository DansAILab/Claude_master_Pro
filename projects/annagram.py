def are_anagrams(text1, text2): 
    counts1 = {} 
    counts2 = {} 

    for count in text1:
        if count in counts1:
            counts1[count] = counts1[count] + 1
        else:
            counts1[count] = 1

    for count in text2:
        if count in counts2:
            counts2[count] = counts2[count] + 1
        else:
            counts2[count] = 1

# fill counts1 with letter counts from text1 
# (same pattern as before: check if letter exists, +1 or start at 1) 

# fill counts2 with letter counts from text2 
# (same pattern) 

# now compare counts1 and counts2 — are they exactly equal? return ___ 
    if counts1 == counts2: 
        return True
    else:
        return False

print(are_anagrams("listen", "silent")) 
print(are_anagrams("hello", "world"))