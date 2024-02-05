""" list is the most versatile datatype in python
depends on sequence
"""
""" loosely dynamic typed lang."""
"""1- to define a list"""

l = []
myl = list()

""" list can hold different data from different datatypes """
myl = ["ahmed", "iti", True, 434.344, 434, ["python", "django"], "iti", None]

"""get len of list ?"""
print(len(myl))

""" count element occurrence in list"""
print(myl.count("iti"))

""" get element index in list  """
print(myl.index("iti"))  # index first occurrence of the element

""" access element using index"""
print(myl[2])
print(myl[5][1])
""" list is mutable datatype """
myl[7] = "updated"
print(myl)
# myl[100] = 'updated value'  # IndexError: list assignment index out of range

""" add element to the list --->  """
myl.append("new element")  # add element to the end of the list
print(myl)

""" insert element at certain index """
myl.insert(4, "inserted element")

""" remove element from the list """
print(myl)
popped_element = myl.pop()  # return with the popped element --> pop last element in the list
print(popped_element)
print(myl)

""" pop element at certain index """

popped_element = myl.pop(3)  # return with the popped element -->pop element at index
print(popped_element)
print(myl)

"""remove certain element """
myl.remove("iti")  # remove first occurence
print(myl)
# myl.remove("noha")
""" concat the list """
courses = ["Python", "Django", "flask"]
basics = ["linux", "bash", "git", 4324, True]

track_courses = courses + basics  # return new list

""" extend a list ?  """
courses.extend(basics)
print(courses)  # extend the content of courses list by the content of basics

""" sort the list  ---> comparison ---> you can only compare items from the same type """
basics = ["linux", "bash", "git"]
# basics.sort()
# print(basics)
#### sorted --> check the difference on your own
basics.sort(reverse=True)
print(basics)

# myl = [235,53,435,24,2434]
# myl.sort()
# print(myl)
# myl.sort()
"reverse a list "
print(myl)
myl.reverse()
print(myl)

""" loop over the list ? """
# print("ahmed")
# print("Ali")
for item in myl:
    print(f"item = {item}")

""" item , index """
index = 0
for abbass in myl:
    print(f"{index}: {abbass}")
    index +=1

""" enumerate fun"""

# generate _index , item --> loop
enum_list = enumerate(myl)   # <enumerate object at 0x7f5210bb6020>
print(enum_list)
# """ enumerate object ---> can be looped over """
# for myindex , myitem in enum_list:
#     print(f"index= {myindex}, item = {myitem}")

""" cast enumerate to list """
# list_items_index = list(enum_list)
# print(list_items_index)

for index, char  in enumerate("noha"):
    print(f"{index}: {char}")
""" cast string to list """
message = 'python'
message = list(message)
print(message)

""" split string to a list """
greeting = "nice to meet you"  # ["nice", "to", "meet", "you"]
greeting_message = greeting.split(" ")
print(greeting_message)
"""join list elements into one string --> list consists of strings  """
students = ["ahmed",  "Mohamed", "test"]
students_info = "_".join(students)
print(students_info)

""" min , max ---> list elements must be from the same type  """

print(min("hassan", "Mohamed", "Hassan", "abc", "ITI"))  # ascii codeeeeee
