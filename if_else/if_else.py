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



#While Loops
my_girlfriend = 0
gf_list = []

while my_girlfriend < 13:
    print(f"Babe let's count my ex's: {my_girlfriend}")
    gf_list.append(my_girlfriend) # The append() method adds a single item to the end of the list.

    my_girlfriend = my_girlfriend + 1

    print("So Counting my ex's no. ", gf_list)
    print(f"and still counting... {my_girlfriend}")

print("Final list till now: ")

for my_girls in gf_list:
    print(my_girls)