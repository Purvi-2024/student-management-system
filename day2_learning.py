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
# class car:  */class*/
#     pass
# class car:    */object*/
#     my_car=car()
# class car:
#     def __init__(self,brand):
#         self.brand = brand      # attribute(data)
#     def drive(self):
#         return "vroom!"         # method(action)
# tesla = car("tesla")
# print(tesla.brand) #output:tesla
# print(tesla.drive()) #output:vroom!
# class Vehicle:         //inheritance example
#     def turn_on(self):
#         return "Engine Started"
# class ElectricCar(Vehicle):
#     pass


# leaf = ElectricCar()
# print(leaf.turn_on())
# class Dog: //polymorphism example
#     def speak(self):
#         return "Woof!"
# class Cat:
#     def speak(self):
#         return "meow!"
# for animal in [Dog(),Cat()]:
#     print(animal.speak())
# class BankAccount:        //encapsulation example
#     def __init__(self,balance):
#         self.__balance=balance
# account = BankAccount(1000)
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_average(self):
#         sum=0
#         for val in self.marks:
#             sum+= val
#         print("hi",self.name,"your avg score is:",sum/3)
# s1 = Student("tony",[99,98,97])
# s1.get_average()
# class Student: //static method
#     @staticmethod
#     def college():
#         print("Abc college")
# class car:        //abstraction example
#     def __init__(self):
#         self.acc = False
#         self.brk = False 
#         self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print ("car started..")
# car1 = car()
# car1.start()
# class Account:     //encapsulation example
#     def __init__(self,balance,account_number):
#         self._balance=balance
#         self._account_number=account_number
#     #debit method
#     def debit(self,amount):
#         self._balance -= amount
#         print("Rs.",amount,"Was debited")
#         print("Your current balance is:",self._balance)

#     def credit(self,amount):
#         self._balance += amount
#         print("Rs.",amount,"Was credited")

#     def get_balance(self):
#         return self._balance
    
# acc1 = Account(1000,12343)
# print(acc1._balance)
# print(acc1._account_number)
# acc1 = Account(10000,12345)
# acc1.debit(500)
# acc1.credit(2998)