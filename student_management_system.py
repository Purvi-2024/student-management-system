students = {}

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
        sid = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        students[sid] = {
            "name": name,
            "course": course,
            "marks": marks
        }

        print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No Students Found")

        else:

            for sid, details in students.items():

                print("\nStudent ID:", sid)
                print("Name:", details["name"])
                print("Course:", details["course"])
                print("Marks:", details["marks"])

    elif choice == "3":

        sid = int(input("Enter Student ID: "))

        if sid in students:
            print(students[sid])

        else:
            print("Student Not Found")

    elif choice == "4":

        sid = int(input("Enter Student ID: "))

        if sid in students:

            students[sid]["name"] = input("Enter New Name: ")
            students[sid]["course"] = input("Enter New Course: ")
            students[sid]["marks"] = float(input("Enter New Marks: "))

            print("Student Updated Successfully!")

        else:
            print("Student Not Found")

    elif choice == "5":

        sid = int(input("Enter Student ID: "))

        if sid in students:

            del students[sid]

            print("Student Deleted Successfully!")

        else:
            print("Student Not Found")

    elif choice == "6":

        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
