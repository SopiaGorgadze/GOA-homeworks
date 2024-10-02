# დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი უარყოფითი ან  ლუწი.
 
num = int(input("enter a number: "))

if num < 0:
    print("this number is negative")
elif num % 2 == 0:
    print("this number is even")
else:
    print("this number is neither")