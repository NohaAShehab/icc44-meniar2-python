"""
    encapsulation ---> who can see what ?
    object --> way of encapsulation --->

    access modifiers

    public  ==> property/ method ---> can be accessed anywhere using instance
    protected ==> property/ method ---> can be accessed anywhere in the class
        or derived classes  using instance
    private  ==> property/ method ---> can be accessed only in the class

    ==> setter and getters

    -----------------------NO ACCESS MODIFIER IN PYTHON  -----------------------------
    ===> access modifiers  --> naming of variable/ method
    a-->z ===> public
    _[a===>z] ===> protected
    __[a===>z] ===> private

"""

# class Employee:
#
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary
#
#
#     def printEmpInfo(self):
#         print(f"name={self.name}, email={self._email}, salary={self.__salary}")
#
#
# emp1 = Employee("Ahmed", "Ahmed@gmail.com", 48978)
# emp1.printEmpInfo()
#
# ### access public property
# print(emp1.name)
# emp1.name = 'updated'
# ### protected
# ## python developer is mature
# print(emp1._email)    # ethically don't do this
# emp1._email  ="iowur@fff.com"
#
#
# """ what about private """
# # print(emp1.__salary)  # AttributeError: 'Employee' object has no attribute '__salary'
# print(emp1._Employee__salary)  # ethically don't do this // clean code// don't do this
# print(emp1.city)


""" access modifier ---> setters and getters  """
# class Employee:
#
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary  ##private
#
#
#     def printEmpInfo(self):
#         print(f"name={self.name}, email={self._email}, salary={self.__salary}")
#
#     ## get_salary, set_salary ==> modify or get property value
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self, salary):
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary >0 :
#             self.__salary = salary
#         else:
#             raise  ValueError('Salary must be positive number ')
#
#
#
# emp1 = Employee("Ahmed", "Ahmed@gmail.com", 48978)
# # print(emp1.__salary)
# print(emp1.get_salary())
# emp1.set_salary(100000)
""" ------------------------------- """


# class Employee:
#
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary  ##private
#
#     def printEmpInfo(self):
#         print(f"name={self.name}, email={self._email}, salary={self.__salary}")
#
#     ## get_salary, set_salary ==> modify or get property value
#     def get_salary(self):
#         return self.__salary
#
#     @property  # this function get value from property
#     def salary(self):
#         return self.__salary
#
#     def set_salary(self, salary):
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary > 0:
#             self.__salary = salary
#         else:
#             raise ValueError('Salary must be positive number ')
#
#
# emp1 = Employee("Ahmed", "Ahmed@gmail.com", 48978)
# # print(emp1.__salary)
# print(emp1.get_salary())
# emp1.set_salary(100000)
#
# print(emp1.salary)
#
# emp1.salary = 489389357  # AttributeError: property 'salary' of 'Employee' object has no setter
#
#


class Employee:

    def __init__(self, name, email, salary):
        self.name = name
        self._email = email
        self.__salary = salary  ##private

    def printEmpInfo(self):
        print(f"name={self.name}, email={self._email}, salary={self.__salary}")

    @property  # this function get value from property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if (isinstance(salary, int) or isinstance(salary, float)) and salary > 0:
            self.__salary = salary
        else:
            raise ValueError('Salary must be positive number ')

    def set_salary(self, salary):
        if (isinstance(salary, int) or isinstance(salary, float)) and salary > 0:
            self.__salary = salary
        else:
            raise ValueError('Salary must be positive number ')


emp1 = Employee("Ahmed", "Ahmed@gmail.com", 48978)
emp1.set_salary(100000)

print(emp1.salary)

emp1.salary = 489389357
