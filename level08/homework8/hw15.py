# მომხმარებლის შემოტანილი რიცხვი შეამოწმე, არის თუ არა  20-ის ჯერადი და დადებითი.

num = int(input("enter a num: "))

if num %20 == 0 and num > 0:
    print("this number can be divided on 20 and is positive")
elif num %20 != 0 and num > 0:
    print("this number cannot be divided on 20 but is positive")
else:
    print("this number cannot be divided on 20 and is negative")