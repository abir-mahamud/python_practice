<<<<<<< HEAD
# while loop
i = 20
while i > 1:
    print(i)
    i -= 2

i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    print(i)
print("i is no longer less than 10")


# printing stars
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()


for i in range(10):
    print(" "*(10-i) + "*" * i)

for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()


for i in range(0, 5):
    print(" "*(5-i)+"* "*i)
for i in range(5, 0, -1):
    print(" "*(5-i)+"* "*i)


for i in range(5, 0, -1):
    print(" "*(5-i)+"* "*i)


for i in range(5, 0, -1):
    print("  "*(5-i)+"* "*i)


for i in range(5, 0, -1):
    print("* "*i)

for i in range(5):
    print("* "*i)
=======
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
>>>>>>> 29d4d78c024235fb820431fc9be963fdddc2ff82
