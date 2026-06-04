import numpy as np


class Student:

    def __init__(self, sid, name, course, marks):
        self.sid = sid
        self.name = name
        self.course = course
        self.marks = marks

    def calculate_grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 60:
            return "C"

        else:
            return "D"

    def display(self):

        print("\nStudent ID:", self.sid)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


class StudentManagement:

    def __init__(self):
        self.students = {}

    def add_student(self):

        try:
            sid = int(input("Enter Student ID: "))

            if sid in self.students:
                print("Student ID already exists!")
                return

            name = input("Enter Student Name: ")
            course = input("Enter Course: ")

            marks = float(input("Enter Marks: "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100")
                return

            student = Student(sid, name, course, marks)

            self.students[sid] = student

            print("Student Added Successfully!")

        except ValueError:
            print("Invalid Input! Please enter correct values.")

    def view_students(self):

        if len(self.students) == 0:
            print("No Students Found")
            return

        for student in self.students.values():
            student.display()

    def search_student(self):

        try:
            sid = int(input("Enter Student ID: "))

            if sid in self.students:
                self.students[sid].display()

            else:
                print("Student Not Found")

        except ValueError:
            print("Please enter a valid Student ID")

    def update_student(self):

        try:
            sid = int(input("Enter Student ID: "))

            if sid in self.students:

                student = self.students[sid]

                student.name = input("Enter New Name: ")
                student.course = input("Enter New Course: ")

                marks = float(input("Enter New Marks: "))

                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100")
                    return

                student.marks = marks

                print("Student Updated Successfully!")

            else:
                print("Student Not Found")

        except ValueError:
            print("Invalid Input!")

    def delete_student(self):

        try:
            sid = int(input("Enter Student ID: "))

            if sid in self.students:

                del self.students[sid]

                print("Student Deleted Successfully!")

            else:
                print("Student Not Found")

        except ValueError:
            print("Invalid Student ID")

    def total_students(self):

        print("Total Students:", len(self.students))

    def average_marks(self):

        if len(self.students) == 0:
            print("No Students Found")
            return

        marks = []

        for student in self.students.values():
            marks.append(student.marks)

        avg = np.mean(marks)

        print("Average Marks:", round(avg, 2))

    def find_topper(self):

        if len(self.students) == 0:
            print("No Students Found")
            return

        topper = max(
            self.students.values(),
            key=lambda student: student.marks
        )

        print("\n===== TOPPER DETAILS =====")

        topper.display()


sms = StudentManagement()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Average Marks")
    print("8. Find Topper")
    print("9. Exit")

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
        sms.total_students()

    elif choice == "7":
        sms.average_marks()

    elif choice == "8":
        sms.find_topper()

    elif choice == "9":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")