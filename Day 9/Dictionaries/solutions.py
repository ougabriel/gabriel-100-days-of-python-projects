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
#Loop through each students scores and store the value
for student in student_scores:
    score = student_scores[student]     #calls the value of each student and stores it as score variable

#The grading logic
    if score >= 91:
        grades = "Outstanding"
    elif score >= 81:
        grades = "Exceeds Expectations"
    elif score >= 71:
        grades = "Acceptable"
    else:
        grades = "Fail"
    

#TO-DO: Assign the grades
    student_grades[student] = grades

#print student grades
student_grades = {}

    

