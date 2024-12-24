# დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი ან 3-ის ჯერადი.

num1 = int(input("please enter your number: "))

if num1 % 2 == 0:
    print("your number is even")
elif num1 % 3 == 0:
    print("your number can be divided on 3")
else:
    print("your number is incorrect")