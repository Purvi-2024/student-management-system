# class student: */making a class*/
#     pass
# class student: */making a object*/
#     pass
# s1=student()
# s2=student()
# class student:   */making a constructor*/
#     def __init__(self):
#         print("constructor called")
#         s1=student()
# class student:   
    # def __init__(self):
    #     print("constructor called")
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         s1=student("sachin",100)
# class student: */example of using constructor to initialize attributes and methods to calculate average and display report*/
#     def __init__(self, name, roll_number, grades):
#         self.name = name
#         self.roll_number = roll_number
#         self.grades = grades

#     def calculate_average(self):
#         if not self.grades:
#             return 0
#         return sum(self.grades) / len(self.grades)

#     def display_report(self):
#         average = self.calculate_average()
#         status = "passed" if average >= 60 else "failed"

#         print("--- student report ---")
#         print(f"student name: {self.name}")
#         print(f"roll number: {self.roll_number}")
#         print(f"average: {average:.2f}%")
#         print(f"status: {status}\n")


# student1 = student("sachin", 101, [85, 92, 78])
# student2 = student("riya", 102, [55, 42, 61])

# student1.display_report()
# student2.display_report()
class student:
    def __init__(self,name):
        self.name=name
        def display(self):
            print(self.name)