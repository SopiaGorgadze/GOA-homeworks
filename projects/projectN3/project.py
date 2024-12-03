# calculator project

num1 = int(input("enter number: "))
operation = input("enter mathematical operation: ")
num2 = int(input("enter number: "))

def addition():
    return num1 + num2

def subtraction():
    return num1 - num2

def multiplication():
    return num1 * num2

def division():
    if num2 == 0:
        return "Error"
    return num1 / num2

if operation == "+":
    print (f"{addition()}")
elif operation == "-":
    print(f"{subtraction()}")
elif operation == "*":
    print(f"{multiplication()}")
elif operation == "/":
    print(f"{division()}")
else:
    print("Error")