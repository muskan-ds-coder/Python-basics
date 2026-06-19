# if-else (11-20)

# Q11 Find the larger of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest number is a:",a)
else:
    print("Largest number is a:",b)

# Q12 Check whether a number is even or odd.
c = int(input("Enter a number: "))
if c%2 == 0:
    print("even.")
else:
    print("odd.")

# Q13 Check if a year is a leap year (basic version).
year = int(input("Enter a year: "))
if year % 4 == 0:
    print("Leap year. ")
else:
    print("Not leap year. ")

# Q14 Check if a person can enter a movie (age >= 18).
age = int(input("enter you'r age: "))
if age >= 18:
    print("you can watch a movie.")
else:
    print("you cannot watch a movie.")

# Q15 Check if a number is positive or negative.
number = int(input("Enter a number: "))
if number >= 0:
    print("Positive number.")
else:
    print("Negative number.")

# Q16 Find whether a number is divisible by both 3 and 5.
number1 = int(input("Enter a no:"))

if (number1 % 3) == 0 and (number1 % 5):
    print("divisible number.")
else:
    print("not divisible number.")

# Q17 Compare two strings and print whether they are equal.
name1 = input("what is your favorite color: ")
name2 = input("what is your favorite clothes color: ")
if name1 == name2:
    print("same")
else:
    print("not same")

# Q18 Check whether a password matches a predefined password.
predefined_password = input("Enter a password: ")
if predefined_password == "muskan123":
    print("predefined password.")
else:
    print("not predefined password.")

# Q19 Check whether a temperature is above 30°C.
temperature = int(input("Enter a today temperature: "))
if temperature > 30:
    print("above.")
else:
    print("not above.")

# Q20 Check if a user has enough balance to buy an item
balance = int(input("Enter your balace: "))
if balance > 5000:
    print("Enough balance to buy an item.")
else:
    print("Not enough balance to buy an item.") 