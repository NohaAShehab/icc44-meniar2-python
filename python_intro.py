"""

    these info will be stored in __doc__  contatins documentation about script

"""
# this is a comment
# define a variable
#
# name = 'ahmed'
# course = 'python'
# Name = 'Noha'
#
# if name == 'ahmed':
#     print('Hello world')
#
# if name == course:
#     pass # represent null operation
#
# print("-----")
#
#
#
# bio = "my name is Noha"
#
# # bio2 = ('My name is Noha '
# #         'I works at ITI'
# #         'I lives in Cairo')
# #
# # print(bio2)
#
# bio2 = ('My name is Noha\n'
#         'I works at ITI\n'
#         'I lives in Cairo')
#
# print(bio2)
#
#
# bio3 = '''My name is Noha
# I works at ITI
# I lives in Cairo
# I love python'''
# print(bio3)
#
# """
#     this is the first python lecture
#     this string acts like a comment
# """

# generate documentation for your application


""" define variable """
#
# name = 'ahmed'
# track = 'python'
# intake = 44  # int
# happy = True  # bool
# g = 9.8  # float
# requirements = None  # No null in python
#
# """ check type of variable ? """
# print(type(name))  # string  ==> object from class str
# print(type(g))
#
# """ type conversion is allowed  """
#
# g = str(g)
# print(g, type(g))
#
# intake = float(intake)
# print(intake, type(intake))
#
#
# "convert bool to string "
# happy  = str(happy)
# print(happy, type(happy))
#
#
# """ convert string to bool"""
#
# name = bool(name)
# print(name, type(name))
#
# """ convert string to int """
# year = '2024'  # string
# year = int(year) #int
#
# track  =int(track)
# print(track, type(track))
#
# """ you convert from string to int only if the string contains numeric value"""
#

""" operators"""

# num1 =10
# num2 = 4
# print(num1 ** num2)  # exponent === power
# num1 += 5  # num1 = num1+5
#
# """ comparison """
#
# print("ahmed"  < "Ahmed")  # compare using ascii code
# """ comparison in python --> compare data from same datatype """
# # print("ahmed"> 10)  #TypeError: '>' not supported between instances of 'str' and 'int'
# # print("10"> 10)
# print('ahmed'> "a10")

# name='ahmed'
# if name != 'ahmed':
#     print("----")
#
#
# print(not "ahmed")
#
# if not name:
#     print("")

#
# print("ahmed" and "iti")  # ahmed --> True  and iti ---> iti
#
# print(False and "iti" and "ahmed")
res = "ahmed" and "iti" and "" and "noha" and False
print(res)

print(False or 0 or None )



course= 'ksjddfj'

if course =='python':
    print("python is easy ")
elif course =='django':
    print('Django is so easy ')
else:
    print("enjoy your course ")

