name = input("Enter your Name: ")
age = int(input("Enter your age: "))
roll_number = input("Enter your Roll Number: ")
physics_marks = float(input("Enter your physics Marks: "))
chemistri_marks = float(input("Enter your chemistry Marks: "))
mathematics_marks = float(input("Enter your mathematics Marks: "))

print("\n----- Student Details -----\n")
print("Name:", name)
print("Age:", age)
print("Roll Number:", roll_number)
print("Physics Marks:", physics_marks)
print("Chemistry Marks:", chemistri_marks)
print("Mathematics Marks:", mathematics_marks)

total_marks = physics_marks + chemistri_marks + mathematics_marks
average_marks = total_marks / 3
percentagemarks = (total_marks / 300) * 100
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)  
print("Percentage Marks:", percentagemarks, "%")
