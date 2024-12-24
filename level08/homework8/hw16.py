# დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი ერთდროულად 50-ზე ნაკლები და 10-ის ჯერადი.

num = int(input("enter a number: "))

if num < 50 and num %10 == 0:
    print("this number is bellow 50 and can be divided on 10")
else:
    print("this number is not bellow 50 or it can not be divided on 10")

