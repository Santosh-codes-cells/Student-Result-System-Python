students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = []

    print("Enter marks for 3 subjects (Maths, Physics, Chemistry):")
    for i in range(3):
        score = float(input("Enter marks: "))
        marks.append(score)

    total = marks[0] + marks[1] + marks[2]
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully.")

def view_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        for s in students:
            print("\nName:", s['name'])
            print("Roll No:", s['roll'])
            print("Marks:", s['marks'])
            print("Total:", s['total'])
            print("Average:", round(s['average'], 2))
            print("Grade:", s['grade'])
            print("------------------------------")

def main():
    while True:
        print("\n--- Student Result Management ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
