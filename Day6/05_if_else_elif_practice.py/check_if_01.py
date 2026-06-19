# if (1-10)

# Q1   Check if a number is positive.
number1 = int(input("Enter a positive number: "))
if number1 >= 0:
    print("number is positive.")


# Q2   Check if a number is negative.
number2 = int(input("Enter a negative number: "))
if number2 <= 0:
    print("number is negative.")


# Q3   Check if a number is zero.
number3 = int(input("Enter a zero number: "))
if number3 == 0:
    print("number is zero.")


# Q4   Check if a number is even.
number4 = int(input("Enter a evevn number: "))
if number4%2 == 0:
    print("even.")

# Q5   Check if a number is odd.
number4 = int(input("Enter a odd number: "))
if number4%2 != 0:
    print("odd.")


# Q6   Check if a person is eligible to vote (18+).
number5 = int(input("Enter you'r age: "))
if number5 >= 18:
    print("eligible.")

# Q7   Check if a student passed (marks >= 35).
student = int(input("Enter marks no.: "))
if student >= 35:
    print("pass.")

# Q8   Check if a number is divisible by 5.
number6 = int(input("Enter divisible no. by 5: "))
if number6 // 5:
    print("number is divisible.")

# Q9   Check if a number is divisible by 10.
number7 = int(input("Enter divisible no. by 10: "))
if number7 // 10:
    print("number is divisible.")

# Q10  Check if a character is uppercase.
name = input("Enter uppercase: ")
if name==name.upper():
    print("Character is uppercase.")