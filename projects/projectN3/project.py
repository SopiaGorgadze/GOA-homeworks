# calculator project

num1 = int(input("enter number: "))
operation = input("enter mathematical operation: ")
num2 = int(input("enter number: "))

num1 = input()
operation = input()
num2 = input()
def addition():
    print(num1 + num2)
def substraction():
    print(num1 - num2)
def multy():
    print(num1 * num2)
def division():
    print(num1 / num2)

if operation == "+":
    print(addition())
elif operation == "-":
    print(substraction())
elif operation == "*":
    print(multy())
elif operation == "/":
    print(division())