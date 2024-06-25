class_score = float(input("Enter your class score (out of 100): "))
if class_score >= 90:
    letter_grade = "A"
elif class_score >= 80:
    letter_grade = "B"
elif class_score >= 70:
    letter_grade = "C"
elif class_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
print("Your letter grade is:", letter_grade)
