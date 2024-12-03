# daily routine project



c = 0


print("-" * 30)
print("hello this is a python project that can help you manage your daily routine")
print("-" * 30)
print("are you open with working with me?")
print(" " * 30)
answ = input("enter your answer here: ")
if answ == "no":
    print("okay goodbye")
else:
    print(30 * "-")
    print("okay lets begin! ")
    print(30 * " ")

    st = input("are you a student or do you have a job?: ")
    if st == "no":
        print(30 * " ")
        print("get out of here you unemployed pig")
    else:
        start = int(input(" at what time do you start your day?: "))
        print(30 * " ")
        start1 = int(input("at what time do you leave the house?: "))
        print(30 * " ")
        c = c + start1
        start2 = int(input("how long does your work or school hours last?: "))
        print(30 * " ")
        c = c + start2
        start3 = input("if you go to school, do you have other subjects that you go to after school?: ")
        if start3 == "yes":
            print(30 * " ")
            subj = input("what subject?: ")
            print(30 * " ")
            tim = int(input("at what time do you get there?: "))
            c = c + tim
            print(30 * " ")
            hour = int(input("how many hours does it last?: "))
            c = c + hour
        else: 
            print(" " * 30)
    print("-" * 30)
    print("okay here's your schedule: ")
    print(" " * 30)

    print("1. wake up at: " + str(start) + ":00 AM")
    print("2. leave the house at: " + str(start1)+ ":00 AM")
    print(f"3. school/work ends at:  {c - tim - hour}:00 o'clock")
    print("4. " +str(subj)+ " starts at: " + str(c - tim)+":00 o'clock")
    print(f"5. you should get home at: {c - tim + hour}:00 o'clock")
    print(" " * 30)
    print("-" * 30)
     