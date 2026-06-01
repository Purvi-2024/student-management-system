# Student Management System

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    students[roll] = name
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
    else:
        print("Student Records:")
        for roll, name in students.items():
            print(f"Roll No: {roll}, Name: {name}")
        print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print(f"Student Found: {students[roll]}\n")
    else:
        print("Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

while True:
    print("---- Student Management System ----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
