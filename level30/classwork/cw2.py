
# num = 10
# num1 = 20

# def multiply():
#     print(num * num1)

# def sum():
#     print(num + num1)

# def min():
#     print(num - num1)
 
# def divide():
#     return 10 / 2
     

# # use return not print
# print(divide())


 

# # def list():
# #     list = [1, 2, 3, 4, 5]
# #     return sum(list)
  
# # print(list())



# def sum():
#     numbers_list = [1, 2, 3, 4, 5,]
#     numbers_sum = 0
#     for i in range(len(numbers_list)):
#         numbers_sum += numbers_list[i]

#         return numbers_sum
    

# print(sum())






# პარამეტრი
# არგუმენტი


def plus(a, b):     #პარამეტრი
    return a + b

print(plus(5, 7))    #არგუმენტი
print(plus(1, 2))


def greet(name, lastname):
    return "hello", name, lastname

print(greet("sofia", "gorgadze"))



def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(even_or_odd(5))


