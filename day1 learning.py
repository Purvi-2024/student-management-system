# def add_numbers(*args):
#     print(args)
#     return sum (args)
# result = add_numbers(10,20,30,40)
# print(result)
# def student_info(**kwargs):
#     print(kwargs)
# student_info(name="purvi",age=20,course="cse")
# def display(*args,**kwargs):
#     print("Args:",args)
#     print("kwargs:",kwargs)
# display(1,2,3,name="purvi",branch="cse")
# fruits=["apple","mango","banana"]
# print(fruits[0])
# print(fruits.append("orange"))
# print(fruits)
# fruits=("apple","mango","banana")
# print(fruits[0])
# print(fruits[1]="grapes")
# student={"name":"purvi","age":20,"course":"cse"}
# print(student["name"])
# student["college"]="xyz"
# print(student)
# student["age"]=21
# print(student)
# my_dict={(1,2,3):"hello"
#          }
# print(my_dict[(1,2,3)])
# d1={"a":1,"b":2}
# d2={"b":2,"a":1}
# print(d1==d2)
# def show(*args):
#     print(type(args))
#     show(1,2,3)
# try:       /*division by zero error*/
#     a=int(input("enter number:"))
#     b=int(input("enter divisor:"))
#     result=a/b
#     print(result)
# except ZeroDivisionError:
#     print("Division by zero not allowed")
# try:      /*handling multiple exceptions*/
#     num = int(input("Enter a number:"))
#     result =100/num
#     print(result)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("please enter only numbers")
# try:                                    /*using else block*/
#      a= int(input("Enter first num"))
#      b=int(input("Ebter second number:"))
#      result = a/b
# except ZeroDivisionError:
#      print("cannot divide by zero")
# else:
#      print("Result =",result)
# try:
#     file = open("sample.txt")
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("Program Ended")