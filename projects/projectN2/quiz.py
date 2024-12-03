# quiz project

answ = input("are you ready to take this quiz?: ")


count = 0


print(" " * 10)
if answ == "no":
    print("okay goodbye.")
else:
    print("okay lets start!")
    print("-" * 30)
    print("question number 1!")
    print(" " * 30)
    print("1. Who was the first president of the United States?")
    print("------ 1.Donald Trump")
    print("------ 2. George Washington")
    print("------ 3. George W. bush")
    print("please enter the number of your answer ")
    answ1 = int(input("here: "))
    if answ1 == 2:
        print("well done! youre right.")
        count = count + 1
    else:
        print("wrong!")
        print(" " * 30)
    print("-" * 30)
    print("question number 2!")
    print(" " * 30)
    print("2. What year did World War II end?")
    print("------ 1. 1945")
    print("------ 2. 1918")
    print("------ 3. 1939")
    print("please enter the number of your answer ")
    answ2 = int(input("here: "))
    if answ2 == 1:
        print("well done! youre right.")
        count = count + 1
    else:
        print("wrong!")
    print("-" * 30)
    print("question number 3!")
    print(" " * 30)
    print("3. Which country is known as the Land of the Rising Sun?")
    print("------ 1. Finland")
    print("------ 2. Brazil")
    print("------ 3. Japan")
    print("please enter the number of your answer ")
    answ3 = int(input("here: "))
    if answ3 == 3:
        print("well done! youre right.")
        count = count + 1
    else:
        print("wrong!")
    print("-" * 30)
    print("question number 4!")
    print(" " * 30)
    print("4. What is the closest planet to the Sun?")
    print("------ 1. Mercury")
    print("------ 2. Venus")
    print("------ 3. Jupiter")
    answ4 = int(input("here: "))
    if answ4 == 1:
        print("well done! youre right.")
        count = count + 1
    else:
        print("wrong!")
    print("-" * 30)
    print("question number 5!")
    print(" " * 30)
    print("5. In which year did the Berlin Wall fall?")
    print("------ 1. 1988")
    print("------ 2. 1989")
    print("------ 3. 1978")
    print("please enter the number of your answer ")
    answ5 = int(input("here: "))
    if answ5 == 2:
        print("well done! youre right.")
        count = count + 1
    else:
        print("wrong!")
    print("-" * 30)
    print("question number 6!")
    print(" " * 30)
    print("6. What is the most common blood type in humans?")
    print("------ 1. O positive")
    print("------ 2. B negative ")
    print("------ 3. A positive ")
    print("please enter the number of your answer ")
    answ6 = int(input("here: "))
    if answ6 == 1:
        print("well done! youre right.")
        count = count + 1
    else:
        print("wrong!")
    print("-" * 30)
    print("question number 7!")
    print(" " * 30)
    print("7. Which empire was the largest contiguous empire in history?")
    print("------ 1. British Empire")
    print("------ 2. Mongol Empire")
    print("------ 3. Russian Empire")
    print("please enter the number of your answer ")
    answ7 = int(input("here: "))
    if answ7 == 2:
        print("well done! youre right.")
        count = count + 1
    else:
        print("wrong!")
    print(f" your correct answers were {count} out of 7")






