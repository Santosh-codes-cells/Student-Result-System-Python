students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = []
    subjects = ["Maths", "Physics", "Chemistry"]

    for subject in subjects:
        score = float(input(f"Enter marks for {subject}: "))
        marks.append(score)

    total = sum(marks)
    average = total / len(subjects)

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
    print("\nstudent added successfully!\n")

def view_students():
    if not students:
        print("No student records found.")
        return

    for s in students:
        print(f"\nName: {s['name']}")
        print(f"Roll No: {s['roll']}")
        print(f"Marks: {s['marks']}")
        print(f"Total: {s['total']}")
        print(f"Average: {s['average']:.2f}")
        print(f"Grade: {s['grade']}")
        print("-" * 30)

def main():
    while True:
        print("\n--- Student Result Management ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()