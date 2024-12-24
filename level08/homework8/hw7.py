# დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა მომხმარებლის რიცხვი 0-ზე ნაკლები.

num1 = int(input("enter a number: "))

if num1 < 0:
    print("your number is less than 0")
elif num1 == 0:
    print("your number is 0")
else:
    print("your number is greater than 0")