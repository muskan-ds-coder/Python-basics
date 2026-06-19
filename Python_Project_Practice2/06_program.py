# find largest Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    print("largest =", a)
elif b > c:
    print("Largest =", b)
else:
    print("Largest =", c)

if a > b:
    print("largest =", a)
else:
    print("Largest =", b)

a = 10
b = 20
c = 25
if a < b and a < c:    # true and true = true
    print("L =", c)
else:
    print("L =", b)


def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum * 2
    return sum
  else:
    return sum
  

def sum_double(a, b):
  sum = 0
  if a == b:
    sum = (a * 2) + (b * 2)
    return sum
  else:
    sum = (a+b)
    return sum

num = int(input("Enter a number: "))

if num >= 35:
   print("Pass")

