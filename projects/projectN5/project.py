year_of_birth = int(input("what's your birth year?: "))
print("-" * 30)
current_year = 2024

def calculate_age(year_of_birth, current_year):
    ty = current_year - year_of_birth
    if ty == 1:
            return "You are "+str(ty)+ " year old."
    elif ty > 1:
            return "You are "+str(ty)+ " years old."  
    elif ty == 0:
            return "You were born this very year!"
    elif ty == -1:
        ty = -ty
        return "You will be born in " + str(ty) + " year."
    elif ty < 0:
        ty = -ty
        return "You will be born in " + str(ty) + " years."
    else:
        return "error"
    
print(calculate_age(year_of_birth, current_year))
            