

""" single inheritance """

# class Person:
#     pass
#
#
# class Employee(Person):  # employee class inherits from Person
#     pass
#
#
# emp = Employee()
# # check if emp isinstance from person
# print(isinstance(emp, Person))
# print(isinstance(emp, object))


""" 2nd scenario """
# class Person:
#     def __init__(self, name):
#         self.name =name
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# class Employee(Person):  # employee class inherits from Person
#     pass
#
#
# emp = Employee("noha")
# emp.speak()
#

""" 3rd scenario """

# class Person:
#     def __init__(self, name):
#         self.name =name
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# class Employee(Person):  # employee class inherits from Person
#     def __init__(self,name, salary):
#         # call parent constructor
#         super().__init__(name)
#         self.salary = salary
#
#
# emp = Employee("noha", 82934)
# emp.speak()

#
# """ third scenario """
# class Person:
#     def __init__(self, name):
#         self.name =name
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
#
#
#
#
# class Employee(Person):  # employee class inherits from Person
#     def __init__(self,name, salary):
#         # call parent constructor
#         super().__init__(name)
#         self.salary = salary
#
#     # overriding
#     def speak(self):
#
#         print(f"My salary is {self.salary}")
#
# emp = Employee("noha", 82934)
# emp.speak()
#
#
#
#
#
#
#
#




##############################################

""" multiple inheritance """

# class Engineer:
#     pass
#
#
# class Employee:
#     pass
#
#
# class Instructor(Employee, Engineer):
#     pass

# inn = Instructor()
# print(isinstance(inn, Employee))
# print(isinstance(inn, Engineer))
""""   2nd scenario"""
# class Engineer:
#     pass
#
# class Employee:
#     def __init__(self):
#         print("I am an employeee")
#
# class Instructor(Employee, Engineer):
#     pass
#
#
#
#
#
# inn = Instructor()

""" 3rd scenario """
# class Engineer:
#     def __init__(self):
#         print("I am Engineer")
#
# class Employee:
#     pass
#     # def __init__(self):
#     #     print("I am an employeee")
#
# class Instructor(Employee, Engineer):
#     pass
#
#
# inn = Instructor()

""" the last one """

class Engineer:
    def __init__(self):
        print("I am Engineer")

class Employee:
    def __init__(self):
        print("I am an employeee")

class Instructor(Employee, Engineer):
    def __init__(self):
        print("I am an instructor")
        super().__init__()


inn = Instructor()
















