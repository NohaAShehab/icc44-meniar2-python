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

# class Employee(object):  # Employee implicitly inherits from object class
#     def __init__(self, name='', salary=1000):
#         # name and salary  are instance variables
#         self.name =name   # properties
#         self.salary = salary
#
#     # instance method
#     def printEmpInfo(self):
#         print(f"name={self.name}, salary={self.salary}")
#
# emp = Employee("abc", 1000)  # new object
# emp.printEmpInfo()
#
# emp2 = Employee("tttt", 2000)
# emp2.printEmpInfo()
# emp3= Employee()
#
# emp.city= 'Cairo'


############################################################################

""" all employees commission = 10% -->  .1 """
""" commission ---> class variable """

# class Employee:  # Employee implicitly inherits from object class
#     commission = .1  # class variable  represent class property
#
#     # shared property between all class instances
#     def __init__(self, name='', salary=1000):
#         self.name = name  # properties
#         self.salary = salary
#         # using self ---> represent the object
#
#     # instance method
#     def printEmpInfo(self):
#         print(f"name={self.name}, salary={self.salary}")
#
#
# # access class variable using classname
# print(Employee.commission)
#
# emp = Employee("noha")
# emp2 = Employee("Ahmed")
# emp3 = Employee("Ali")
#
# Employee.commission = .3  # modify using class name


""" count objects from the class """
#
# class Employee:  # Employee implicitly inherits from object class
#     commission = .1  # class variable  represent class property
#     count = 0
#
#     # shared property between all class instances
#     def __init__(self, name='', salary=1000):
#         self.name = name  # properties
#         self.salary = salary
#         # using self ---> represent the object
#         Employee.count +=1
#
#     # instance method
#     def printEmpInfo(self):
#         print(f"name={self.name}, salary={self.salary}")
#
#
# # access class variable using classname
# print(Employee.commission)
#
# emp = Employee("noha")
# emp2 = Employee("Ahmed")
# emp3 = Employee("Ali")
#
# Employee.commission = .3  # modify using class name


""" class methods --> represent class behaviour """

# class Employee:  # Employee implicitly inherits from object class
#     commission = .1  # class variable  represent class property
#     count = 0
#
#     # shared property between all class instances
#     def __init__(self, name='', salary=1000):
#         self.name = name  # properties
#         self.salary = salary
#         # using self ---> represent the object
#         Employee.count +=1
#
#     # instance method
#     def printEmpInfo(self):
#         print(f"name={self.name}, salary={self.salary}")
#
#     # # this function represent class itself not the instance
#     @classmethod
#     def get_no_of_employees(cls): # cls --> represent current class
#         print(f"cls {cls}")
#         #return Employee.count
#         return  cls.count
#
#
#
# ### call class method using class NAme
#
# print(Employee.get_no_of_employees())
#
# print(Employee.count)
# # access class variable using classname
# print(Employee.commission)
#
# emp = Employee("noha")
# emp2 = Employee("Ahmed")
# emp3 = Employee("Ali")
#
# Employee.commission = .3  # modify using class name


"""class method """


# class Employee:  # Employee implicitly inherits from object class
#     commission = .1  # class variable  represent class property
#     count = 0
#
#     # shared property between all class instances
#     def __init__(self, name, salary):
#         self.name = name  # properties
#         self.salary = salary
#         Employee.count += 1
#
#     ### save objects to json   --> instance
#
#     # instance method
#     def printEmpInfo(self):
#         print(f"name={self.name}, salary={self.salary}")
#
#     # # this function represent class itself not the instance
#     @classmethod
#     def get_no_of_employees(cls):
#         return cls.count
#
#
#     ## class method is considered to be object factory
#     @classmethod
#     def create_default_object(cls):
#         return  cls("", 0)
#
#     @classmethod
#     def get_saved_objects(cls):
#         pass
#
#
#
# emp = Employee("ahmed", 324234234)
#
#
# emp2 = Employee.create_default_object()


""" check this """


class Employee:  # Employee implicitly inherits from object class
    commission = .1  # class variable  represent class property
    count = 0

    # shared property between all class instances
    def __init__(self, name, salary):
        self.name = name  # properties
        self.salary = salary
        Employee.count += 1

    ### save objects to json   --> instance

    # instance method
    def printEmpInfo(iti):
        print(iti)

    # # this function represent class itself not the instance
    @classmethod
    def get_no_of_employees(myiti):
        print(myiti)


    ## class method is considered to be object factory




emp = Employee("ahmed", 324234234)


emp2 = Employee.create_default_object()










