# Quiz Game

score = 0

print("Welcome to the Quiz Game!")

q1 = input("Q1: Capital of India? ")
if q1.lower() == "delhi":
    score += 1

q2 =input("Q2: 2 + 2 = ? ")
if q2 == "4":
    score += 1

q3 = input("Q3: Python is a language? (yes/no) ")
if q3.lower() == "yes":
    score += 1

print("\n Your Score:", score)