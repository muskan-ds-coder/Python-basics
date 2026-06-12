# Add two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a+b)

# Subtract two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Difference =", a-b)

# Check Even or odd
num = int(input("Enter first number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# find largest Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("largest =", a)
else:
    print("Largest =", b)

# Multiplication Table
num = int(input("Enter a number: "))

for i in range(1,11):
    print(num, "X", i, "=", num * i)

