student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}

#TODO1 
#Takes in a dictionary of student and their scores
student_grades = {}

#TODO2 
#Converts each score into a grade category
highest_score = 0

# Loop through each student and their score
for student in student_scores:
    scores = student_scores[student] 
# The grading logic
    if scores >= 90:
        student_grades[student] = ("Exceptional")
    elif scores >= 80: 
         student_grades[student] = ("Excellent")
    elif scores >= 70:
          student_grades[student] = ("Very Good")
    elif scores >= 60:
          student_grades[student] = ("Good")
    else:
          student_grades[student] = ("Fail")
    
    
#TODO3 
#Prints the name, score and categories of all students.
    print(f"The following student named {student} has a score of {scores} and a grade of {student_grades[student]}. ")

#TODO4
#Find and prints the student with the highest score   
for name, scores in student_scores.items():
     if scores > highest_score:
          highest_score = scores
          top_student = name
print(f"Our Best Student is {top_student} with a score of {highest_score}({student_grades[top_student]})")
          
        
        