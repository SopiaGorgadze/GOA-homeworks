# 3) დაბეჭდეთ 20-დან 50-მდე ყველა ლუწი რიცხვი

for i in range(20, 50):
    if i % 2 == 0:
        print(str(i) + " even")
    else:
        print(str(i) + " odd")

for i in range(20, 51):
    if i % 2 == 0:
        print(i)