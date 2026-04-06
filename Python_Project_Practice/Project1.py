# This python project will use:
'''
    •	✅ Variables
	•	✅ Strings & characters
	•	✅ Numbers
	•	✅ Comments
	•	✅ Statements
	•	✅ String slicing
	•	✅ String methods (modify string)
	•	✅ Concatenation
	•	✅ Formatting
	•	✅ Escape characters
	•	✅ None (empty variable)
	•	✅ Type casting       
'''
# Student Information Manager

# Variables
name = "Muskan Kumari"
age = "20"      #sttring (we will cast it)
grade = 'A'     #char (singer character)
city = None     #empty varible

# Modify string (capitalize name)
name = name.title()

# Type casting (string to int)
age = int(age)

# Assign value to None vaarible
city = "godda"

# String slicing 
short_name = name[:6]

# Concatenation 
message = "Student: " + name

# Format string
info = f"{message}\nAge: {age}\nGrade: {grade}\nCity: {city}"

# Escape character(\n for new line)
print("----- Student Details -----\n")

# Output statements
print(info)

# String methods
print("\nUppercase Name:", name.upper())
print("Lowercase Name:", name.lower())
print("Short Name:", short_name)
