"""
    class 000> object  --> contains properties

    instance variables ---> instance methods (self---> object address)
    class variables ---> class methods (cls ---> class itself)

"""

# class Employee:
#     commission = .1  # class variables
#     count = 0
#
#     def __init__(self, name, salary):
#         self.name = name  # instance variable
#         self.salary = salary
#         Employee.count += 1
#
#
#     # python consider first argument of function to represent self
#     def printEmpInfo(iti):  # instance method
#         print(iti)
#
#     @classmethod  # first arguemnt of method ---> represent cls
#     def get_no_of_employees(myiti):  # class methods
#         print(myiti)
#     # Usually first parameter of such methods is named 'cls'
#
#
# Employee.get_no_of_employees()
#
# emp = Employee("John", 100000)
# print(emp)
#
# emp.printEmpInfo()


#############################################################3

class Employee:
    commission = .1  # class variables
    count = 0

    def __init__(self, name, salary):
        self.name = name  # instance variable
        self.salary = salary
        Employee.count += 1

    # this is just a helper function
    @staticmethod   # method --> help --> doesn't depend neither object not class
    def cal_net_sal(salary):
        return salary * .8

    def printEmpInfo(self):  # instance method
        print(self.name, self.salary)

    @classmethod
    def get_no_of_employees(cls):  # class method
        print(cls.count)

    def talk(self):
        print(f"My name is  {self.name}")

    @classmethod
    def create_default_object(cls):
        return  cls("emp", 0)


Employee.get_no_of_employees()  # call class method

emp = Employee("John", 100000)
print(emp)
emp.talk()
emp.printEmpInfo()


### function ---> calculate netsalary

def cal_net_sal(salary):
    return  salary*.8


print(cal_net_sal(emp.salary))
print(cal_net_sal(89374893))



print(Employee.cal_net_sal(237874892374))  # calling static method

print(Employee.cal_net_sal(emp.salary))


emp2 = Employee.create_default_object()
print(emp2)









