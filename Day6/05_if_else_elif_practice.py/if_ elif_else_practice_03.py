# # if-elif-else (21-35)

# Find the greatest of three numbers.
a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))
c = int(input("Enter a number 3: "))
if a > b:
    if a < c:
        print("greatest1", c)
    else:
        print("greatest", a)
elif b < c:
    print("greatest", c)
else:
    print("greatest", b)

'''
 Assign grades:
 90-100 → A
 80-89 → B
 70-79 → C
 60-69 → D
 Below 60 → F
''' 
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# Display the day of the week based on a number (1-7).

# Display the month name based on month number.
# Check whether a character is a vowel or consonant.
# Create a simple calculator (+, -, *, /).
# Check traffic light color and print action.
'''
# Categorize age:
# Child
# Teen
# Adult
# Senior
'''
age = int(input("Enter your age: "))
if age <= 12:
    print("child")
elif age <= 17:
    print("Teen")
elif age <= 40:
    print("adult")
else:
    print("Senior")

# Income tax slab calculation.
# Electricity bill calculation based on units.
# Shipping charge based on order amount.
# Login system:
# Username correct?
# Password correct?
# Both wrong?
# BMI category.
# Cricket score result:
# Century
# Half-century
# Low score
# Movie ticket pricing based on age.