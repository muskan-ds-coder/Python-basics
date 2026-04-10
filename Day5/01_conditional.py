# Conditional statements in python
# A conditional statements is used to make decision in a program.
# Used for decision making in a program. It allows us to execute a block of code only if a certain condition is true.

#basic example

x = 10
if x > 5:
    print("x is greater than 5") 

# if statement 
age = 20
if age >= 20:
    print("you are an adult")

# # if-else statement
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

# # if-elif-else statement
marks = 95
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")
'''
# important points
# Condition must be True or False
# use : after condition
# use proper indentation

# if it rains -> take an umbrella
# else -> go normally

# Q1 Check if a number is positive, negative or zero
# Q2 Check if a number is even or odd
# Q3 Take marks and print grade (A, B, C, D, F)'''

x = 5
if x > 0:
    print("Positive")

num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

marks = 31
if marks >= 50:
    print("Grade: A")
elif marks >= 40:
    print("Grade: B")
elif marks >= 35:
    print("Grade: C")
else:
    print("Grade: D")

# boolean values (veri important)
# condition always retrun: True or False
print(5 > 3)
print(2 > 10)

'''comparison opertors
   Used inside conditions

opertor                  Meaning

==                       Equal to
!=                       Not equal to
>                        Greater than
<                        Less than
>=                       Greater than or equal to
<=                       Less than or equal to

'''
x = 10
y = 20
print(x == 10) # True
print(x != 10) # False  
print(10 > 20) # False
print(10 < 20) # True
print(10 >= 10) # True
print(10 <= 20) # True

# Logical Operators
# Used to combine multiple conditions
# operator                 Meaning  
# and                      True if both conditions are true
# or                       True if at least one condition is true
# not                      True if the condition is false
age = 25
print(age > 18 and age < 30) # True
print(age < 18 or age > 30) # False
print(not(age < 18)) # True

print(not True) # False
print(not False) # True

# Nested Conditions
# Condition inside another condition

age = 25
if age >=18:
    if age < 30:
        print("Adult")

# one line if statement
x = 10
if x > 5: print("Greater")

# Ternary Operator(Short if else)
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)


