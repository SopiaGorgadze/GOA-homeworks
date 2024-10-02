# შეამოწმე, არის თუ არა რიცხვი 5-ის ან 10-ის ჯერადი.

num1 = int(input("enter a num: "))

if num1 % 10 == 0:
    print("your number can be divided 10")
elif num1 % 5 == 0:
    print("your number can be divided on 5")
else:
    print("your number cannot be divided on 5")
 