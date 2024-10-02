# დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა მომხმარებლის შემოტანილი რიცხვი 100-ზე მეტი და ლუწი.
num1 = int(input("enter a num: "))

if num1 > 100 and num1 % 2 == 0:
    print("your number is greater than 100 and can be divided on 2")
elif num1 == 100 and num1 % 2 == 0:
    print("your number is equal to 100 and can be divided on 2")
else:
    print("your number is not greater than 100 or cannot be divided on 2")