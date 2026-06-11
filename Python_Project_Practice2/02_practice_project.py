name = input("Your Name: ")
weight = float(input("your Weight(kg): "))
height = float(input("your Height(meters): "))

bmi = weight/(height*height)

if (bmi<18.5):
    print("Underweight")
elif(bmi<28.4):
    print("Normal")
elif(bmi>30.5):
    print("Overweight")
else:
    print("Obese")