# შეამოწმე, არის თუ არა მომხმარებლის შემოტანილი ორი რიცხვი ერთმანეთზე მეტი და 10-ის ჯერადი.
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))

if num1 > num2 and num1 %10 == 0:
    print("num1 is greater than num2 and can be divided on 10")
elif num1 < num2 and num2 %10 == 0:
    print("num2 is greater than num1 and can be divided on 10")
else:
    print("none of this numbers are true")