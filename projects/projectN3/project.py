# calculator project

num1 = int(input("enter number: "))
operation = input("enter mathematical operation: ")
num2 = int(input("enter number: "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num1 == 0:
        print("this action is not supported")
    elif num2 == 0:
        print("this action is not supported")
    else:
        print(num1 / num2)
elif operation == "//":
    print(num1 // num2)
elif operation == "%":
    print(num1 % num2)
else:
    print("this action is not supported")
