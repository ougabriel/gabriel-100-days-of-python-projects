student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

#TO-DO 1: Create an empty dictionary
student_grades = {}

#TO-DO 2: Apply grading logic 
#Loop through each students scores
for student in student_scores:
    scores = student_scores[student]

#The grading logic
    if scores >= 90:
        grades = "Outstanding"
    elif scores >= 80:
        grades = "Exceeds Expectations"
    elif scores >= 71:
        grades = "Acceptable"
    else: grades = "Fail"

#TO-DO: Assign the grades
    student_grades[student] = grades

#print student grades
print(student_grades)


    

