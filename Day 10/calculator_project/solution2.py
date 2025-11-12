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
print("I'm thinking of a number.")
print("\n")
num1 = int(input("What's your first number?: "))

to_continue = True
while to_continue:
    
    for symbols in operations:
        print(symbols)
    operator = input("Pick an operator from the above list: ")
    num2 = int(input("What's the next number. "))
    result = operations[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {result}")

    should_continue = input(f"Type 'yes' to continue calculating with {result}: ") 
    if should_continue.lower() == 'yes':
        num1 = result
    else:
        print("Goodbye!!")
        to_continue = False
