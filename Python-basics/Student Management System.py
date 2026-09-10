students = []


# Add a student
def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("Student added successfully!")


# Display all students
def display_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\n--- Student Details ---")

        for student in students:
            print("Roll No:", student["roll_no"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("----------------------")


# Search student
def search_student():
    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Roll No:", student["roll_no"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            return

    print("Student not found.")


# Delete student
def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Main program
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")