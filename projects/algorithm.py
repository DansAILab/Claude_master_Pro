scores = [85, 92, 78, 90, 88, 66, 95, 100, 72, 84]
grade_counts = {"A": 0, "B": 0, "C": 0, "F": 0}

for score in scores:
        if score >= 90:
            letter = "A"
            grade_counts[letter] = grade_counts[letter] +1 
        elif score >= 80 and score < 90:
            letter = "B"
            grade_counts[letter] = grade_counts[letter] +1
        elif score >= 70 and score < 80:
            letter = "C"
            grade_counts[letter] = grade_counts[letter] +1
        else:
            letter = "F"
            grade_counts[letter] = grade_counts[letter] +1
        
print(grade_counts)
