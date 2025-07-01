#Topic: Nested List and dictionaries

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {
}

for student in student_scores:
    scores = student_scores[student]

    if scores > 90:
        grades = "Outstanding"
    elif scores > 80:
        grades = "Exceeds Expectation"
    elif scores > 70:
        grades = "Acceptable"
    else:
        grades = "Fail"

student_grades[student] = grades

print(student_grades)
