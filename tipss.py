

## FYI

# class Student :
#     def __init__(self, name , age , track):
#         self.name= name
#         self._age = age
#         self.__track = track
#
#
# std = Student("John", 30, "python")
#
# # represent object properties inform of dict
# print(std.__dict__)


# class Student :
#     def __init__(self, name , age , track):
#         self.name= name
#         # self._age = age
#         self.age= age
#         self.__track = track
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         if isinstance(age, int) and age > 0:
#             self._age = age
#         else:
#             raise ValueError("Age must be an integer > 0 ")
#
#
# std = Student("John", 30, "python")
#
# # represent object properties inform of dict
# print(std.__dict__)

""" check this issue """


# class Student :
#     # prevent adding extra properties to the object
#     __slots__ = ('name', '_age', '__track', '__dict__')  # class variable ===> couldn't be changed
#     def __init__(self, name , age , track):
#         self.name= name
#         # self._age = age
#         self.age= age
#         self.__track = track
#         self.__dict__ = {"name":self.name,
#             "_age":self._age, "__track":self.__track}
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         if isinstance(age, int) and age > 0:
#             self._age = age
#         else:
#             raise ValueError("Age must be an integer > 0 ")
#
#
# std = Student("John", 30, "python")
# # std.city = 'cairo'  # AttributeError: 'Student' object has no attribute 'city'
#
#
# # represent object properties inform of dict
# print(std.__dict__)


# Student.__slots__ = ("username","email","age","track")  # don't do this // modify class architecture
# std.city = 'kjfkdj'


""" check this  """


import json
class Student :
    def __init__(self, name , age , track):
        self.name= name
        self.age= age
        self.track= track

    ### models --->
    def __str__(self): # must return with string  # more user-friendly
        return f'{self.name}'

    def __repr__(self):   # must returns with string  # debugging
        # return f'Employee(name={self.name}, age={self.age}, track={self.track})'
        object_info = json.dumps(self.__dict__)  # convert dict to string
        return object_info

    def __len__(self):  # must returns with numbers
        return len(self.__dict__)

    def __call__(self, *args, **kwargs):
        print("--- object is being called ---")



std = Student("John", 30, "python")
""" when you try to print the object --> python check if __str__ exists  if not >>
check if __repr__ exists call it if not >> 
else print address 
"""
# print(std)  # print object address
# print(std.__repr__())

l = [43,56,645,545]
print(len(l))
print(len(std))


## call

# std()  # TypeError: 'Student' object is not callable





