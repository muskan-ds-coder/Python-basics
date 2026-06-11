from turtle import st


students = []

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
    }
    students.append(student)
    print("Student added successfully! ")
def view_student():
    if not students:
        print("No students found.")
        return
    for s in students:
        print(s)

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print("Student Found:", s)
            return
        print("Student not found")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted")
            return
        print("Student not found")

while True:
     print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
     choice = input("Enter choice: ")

     if choice == "1":
         add_student()
     elif choice == "2":
         view_student()
     elif choice == "3":
         search_student()
     elif choice == "4":
         delete_student()
     elif choice == "5":
         break
     else:
         print(" Invalid choice")
