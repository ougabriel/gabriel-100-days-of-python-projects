def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
#Add the functions into a dictionary as the values, keys = '+','-', '*', '/'
operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
}

#Use the dictionary operations to perform the calculations
#Multiply 4 * 8 using the dictionary
print(operations["*"](4, 8))

#Ask the user to type the first and second number
# Program works out the result based on the chosen mathematical operator.
entry1 = int(input("Type any number of your choice: "))
entry_operator = (input("Type any operator of your choice, '+','-', '*', '/': "))
entry2 = int(input("Type second number of your choice: "))
result =  operations[entry_operator](entry1, entry2)
print(f"Your total is: {result}")

# Program asks if the user wants to continue working with the previous result.
# If yes, program loops to use the previous result as the first number and then repeats the calculation process.
# If no, program asks the user for the first number again and wipes all memory of previous calculations.
# Add the logo from art.py

to_continue = (input("Will you like to continue working on the previous result? Type 'Yes' or 'No'")).lower() 
while to_continue == "yes":   
    entry_operator2 = (input("Type any operator of your choice, '+','-', '*', '/': "))
    entry3 = int(input("Type any number of your choice: "))
    new_result = operations[entry_operator2](result, entry3)
    print(f"Your new total is: {new_result}")
    result = new_result

    to_continue = (input("Will you like to continue working? Type 'Yes' or 'No'")).lower()

if to_continue == "no":
    entry4 = int(input("Type any number of your choice: "))
    entry_operator3 = (input("Type any operator of your choice, '+','-', '*', '/': "))
    entry5 = int(input("Type second number of your choice: "))
    result =  operations[entry_operator3](entry4, entry5)
    print(f"Your total is: {result}")
else:
    print("Please type in 'Yes/No': ")



