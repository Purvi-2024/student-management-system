class Student:

    def __init__(self, sid, name, course, marks):
        self.sid = sid
        self.name = name
        self.course = course
        self.marks = marks

    def display(self):
        print("\nStudent ID:", self.sid)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)


class StudentManagement:

    def __init__(self):
        self.students = {}

    def add_student(self):

        sid = int(input("Enter Student ID: "))

        if sid in self.students:
            print("Student ID already exists!")
            return

        name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        student = Student(sid, name, course, marks)

        self.students[sid] = student

        print("Student Added Successfully!")

    def view_students(self):

        if len(self.students) == 0:
            print("No Students Found")
            return

        for student in self.students.values():
            student.display()

    def search_student(self):

        sid = int(input("Enter Student ID: "))

        if sid in self.students:
            self.students[sid].display()
        else:
            print("Student Not Found")

    def update_student(self):

        sid = int(input("Enter Student ID: "))

        if sid in self.students:

            student = self.students[sid]

            student.name = input("Enter New Name: ")
            student.course = input("Enter New Course: ")
            student.marks = float(input("Enter New Marks: "))

            print("Student Updated Successfully!")

        else:
            print("Student Not Found")

    def delete_student(self):

        sid = int(input("Enter Student ID: "))

        if sid in self.students:

            del self.students[sid]

            print("Student Deleted Successfully!")

        else:
            print("Student Not Found")


sms = StudentManagement()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        sms.add_student()

    elif choice == "2":
        sms.view_students()

    elif choice == "3":
        sms.search_student()

    elif choice == "4":
        sms.update_student()

    elif choice == "5":
        sms.delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
