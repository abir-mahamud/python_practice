# list extend
fruits = ["banana", "langraaam", "harivanga"]
favourite = ["mango", "kathal"]
fruits.extend(favourite)
print(fruits)

# if else
age = 40
if age > 10:
    print("maybe teenager")
    if age > 30:
        print("No she is a women ")
    else:
        print("SHIT! buira bedi")

# for loop
names = ["ena", "mena", "tina", "dina"]
for i in names:
    if i == "tina":
        break
    print(i)

names = ["ena", "mena", "tina", "dina"]
for i in names:
    if i == "tina":
        continue
    print(i)


names = ["ena", "mena", "tina", "dina"]
work = ["khaiso?", "ghumaiso?"]
for i in names:
    for j in work:
        print(i, j)