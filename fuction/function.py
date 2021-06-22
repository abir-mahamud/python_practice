# function
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def function(food):
    for i in food:
        print(i)

fruits = ["aam", "jaam", "kola"]
function(fruits)

def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print(f"Let's do some math with just functions!")

age = add(20, 2)
height = subtract(78, 4)
weight = multiply(120, 2)
iq = divide(146, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzel for the extra credit, type it anyway.
print("Here is a puzzel.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes", what, "Can you do it by hand?")



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)