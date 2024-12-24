# 5) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი ფუნქციამ უნდა დაგვიბრუნოს მისი საპირისპირო რიცხვი

num = int(input("enter a num: "))

def opposite(number):
    return number * -1
print(opposite(num))