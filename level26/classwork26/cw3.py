# 1) შექმენით ერთი სია რომელშიც შეიტანთ სახელებს შემდეგ შექმენით მეორე სია რომელშიც იქნება ისევ სხვადასხვა სახელები გააერთიანეთ ეს ორი სია ჩაამატეთ 5 ინდექსზე ახალი სახელი დაითვალეთ გაერთიანებული სიის სიგრძე და დაითვალეთ თქვენი სახელი რამდენჯერ გვხვდება ამ სიაში, ასევე დაბეჭდეთ რომელ ინდექსზე დგას თქვენი სახელი


my_list = ["sofia", "lazare", "nunu",]

my_list2 = ["gio", "luka", "daviti", "nika"]

my_list.extend(my_list2)
print(my_list)

my_list.insert(5, "jamaam")
print(my_list)

my_list.extend(my_list2)
print(my_list)

print(my_list.count("sopia"))

print(my_list.index("sopia"))
 

