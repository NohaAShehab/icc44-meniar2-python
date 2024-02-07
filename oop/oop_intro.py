#
# employee = {
#     "id":1,
#     "name":"ahmed",
#     "email":"ahmed@gmail"
# } # label_Data
#
# emp2 = {
#     "emp_id":2,
#     "first_name":"ali",
#     "emp_email": "ali@gmail.com"
# }
#
#
#
# def printEmployee(emp):
#     print(f"{emp['id']} - {emp['name']} - {emp['email']} -")
#
# printEmployee(employee)
# printEmployee(emp2)
# print(emp2.keys())

"""
        uniform architecture
"""
""" owner datatypes ==> class 

class --> 
"""
name = 'ahmed'
print(isinstance(name, object))

# class Employee:  # Employee implicitly inherits from object class
#     pass
#
#
# print(Employee)
# print(str)

""" =------------------ take an object -------------------------------"""


# class Employee:  # Employee implicitly inherits from object class
#     pass
#
#
# emp = Employee()  # new object
# print(emp)  # <__main__.Employee object at 0x7f5417543dd0>
#
# # loosely dynamically typed lang.
# emp.id = 10
# emp.email = 'ahmed@gmail.com'
# emp.name = 'ahmed'
#
#
# emp2 = Employee()
# emp2.id = 10
# emp2.email = 'mm@gmail.com'
# emp2.empname=  'jdshf'
#
# print(isinstance(emp2, Employee))
# print(isinstance(emp, Employee))

""" ----> """


# __init__ constructor function --->  when you create new object- --> reserve a place in memory
""" customize object creation """
# class Employee(object):  # Employee implicitly inherits from object class
#     def __init__(self):  # self::  represent object add address
#         print(self)
#         print("----- the object is being created -----")
#         # name , salary ---> instance variables
#         self.name = 'ahmed'
#         self.salary = 389247
#
# emp = Employee()  # new object
# print(emp)
# print(emp.name)
# print(emp.salary)
#
# # loosely dynamically
# emp.name  = "updated"
#
#
#
# emp2 = Employee()
# print(emp2)

""" customize value of properties in the object """
# class Employee(object):  # Employee implicitly inherits from object class
#     def __init__(self, name='', salary=1000):
#         # name and salary  are instance variables
#         self.name =name   # properties
#         self.salary = salary
#
# emp = Employee("abc", 1000)  # new object
#
# emp2 = Employee("tttt", 2000)
#
# emp3= Employee()
#
# emp.city= 'Cairo'



""" instance methods ---> its behaviour depends on the caller instance """

class Employee(object):  # Employee implicitly inherits from object class
    def __init__(self, name='', salary=1000):
        # name and salary  are instance variables
        self.name =name   # properties
        self.salary = salary

    # instance method
    def printEmpInfo(self):
        print(f"name={self.name}, salary={self.salary}")

emp = Employee("abc", 1000)  # new object
emp.printEmpInfo()

emp2 = Employee("tttt", 2000)
emp2.printEmpInfo()
emp3= Employee()

emp.city= 'Cairo'