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
