# Student Info Manager (Interactive)

# Taking input (all inputs are strings by default)
name = input("Enter student name: ")
age = input("Enter age: ")
grade = input("Enter grade (A/B/C): ")
city = input("Enter city (press Enter if unknown): ")

# Handle empty input using None
if city == "":
    city = None

# Modify string
name = name.title()

# Type casting
age = int(age)

# String slicing
short_name = name[:4]

# Concatenation
message = "Student: " + name

# Format string
print("\n----- Student Details -----\n")

if city is None:
    info = f"{message}\nAge: {age}\nGrade: {grade}\nCity: Not Provided"
else:
    info = f"{message}\nAge: {age}\nGrade: {grade}\nCity: {city}"

# Output
print(info)

# String methods
print("\nExtra Info:")
print("Uppercase Name:", name.upper())
print("Lowercase Name:", name.lower())
print("Short Name:", short_name)