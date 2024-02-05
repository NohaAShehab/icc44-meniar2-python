""" tuple depends on sequence

tuple like a list --> tuple is immutable ---> once created cannot be changed
"""

"""1- to define a tuple"""

t = ()
myt = tuple()
#
""" tuple can hold different data from different datatypes """
myt = ("ahmed", "iti", True, 434.344, 434, ["python", "django"], "iti", None)
#
"""get len of tuple ?"""
print(len(myt))
#
""" count element occurrence in tuple"""
print(myt.count("iti"))
#
""" get element index in tuple  """
print(myt.index("iti"))  # index first occurrence of the element

""" access element using index"""
print(myt[2])
print(myt[5][1])
# """ tuple is immutable datatype """
# myt[7] = "updated"  # TypeError: 'tuple' object does not support item assignment


""" concat the tuple """
courses = ("Python", "Django", "flask")
basics = ("linux", "bash", "git", 4324, True)
track_courses = courses + basics  # return new tuple
print(track_courses)
#


#
""" loop over the tuple ? """
for item in myt:
    print(f"item = {item}")
#
""" item , index """
index = 0
# for abbass in myt:
#     print(f"{index}: {abbass}")
#     index +=1
#
# """ enumerate fun"""
#
# # generate _index , item --> loop
""" enumerate - -> accept list / string  / tuple ===> generate index for items """
enum_tuple = enumerate(myt)   # <enumerate object at 0x7f5210bb6020>
print(enum_tuple)
# # """ enumerate object ---> can be looped over """
# for myindex , myitem in enum_tuple:
#     print(f"index= {myindex}, item = {myitem}")
# #

""" questions --> answers --> (a,b,c,d )"""
# """ cast enumerate to tuple """
tuple_items_index = tuple(enum_tuple)
print(tuple_items_index)
#

# """ cast string to tuple """
message = 'python'
message = tuple(message)
print(message)
#

# """join tuple elements into one string --> tuple consists of strings  """
students = ("ahmed",  "Mohamed", "test")
students_info = "_".join(students)  # join accept iterable consists of strings /// list/ tuple -->
print(students_info)
#
# """ min , max ---> tuple elements must be from the same type  """
#
print(
    min(
        ("hassan", "Mohamed", "Hassan", "abc", "ITI")
    ))  # ascii codeeeeee


""" tuple of one item """

myinfo = ("iti")
print(myinfo, type(myinfo))

### questions  string - -->accept  answers  ()



