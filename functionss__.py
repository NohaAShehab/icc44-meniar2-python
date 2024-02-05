""" define function """

# def sayhello():
#     pass
#
# res=sayhello()
# print(res)

""" function do something"""
# def sayhello():
#     print("Hello world ")
#
# res=sayhello()
# print(res)

# def sayhello():
#     print("Hello world ")
#     return
#
# res=sayhello()
# print(res)


""" function return somehting """
# def get_fullname():
#     fname= input("Enter your firstName: ")
#     lname= input("Enter your lastName: ")
#     fullname= fname + lname
#     return fullname
#
#
# myname = get_fullname()
# print(myname)
#
# print(get_fullname())

""" return more than one value """

# def get_fullname():
#     fname= input("Enter your firstName: ")
#     lname= input("Enter your lastName: ")
#     fullname= fname + lname
#     return fname, lname, fullname
#
#
# myname = get_fullname()
# print(myname)  # tuple

""" function accept arguments --> return values """

# def sumnum(num1, num2):
#     print(f"num1={num1}, num2= {num2}")
#     res = num1 + num2
#     return res


# ss = sumnum(10 , 20)
# print(ss)

# myres = sumnum(4)  # TypeError: sumnum() missing 1 required positional argument: 'num2'


""" check this scenario """

# def sumnum(num1, num2):
#     print(f"num1={num1}, num2= {num2}")
#     res = num1 + num2
#     return res

# res = sumnum("Ahmed", "Mohamed")
# print(res)
#
# res = sumnum("Ahmed", 23)  #TypeError: can only concatenate str (not "int") to str
# print(res)

""" you must do your the validation """
# def sumnum(num1 :int, num2:int ): # just for documentation purpose
#     print(f"num1={num1}, num2= {num2}")
#     res = num1 + num2
#     return res
#
# res = sumnum("Ahmed", "Mohamed")
# print(res)

""" do your validation """

print(isinstance(10 , int ))
print(isinstance("iti", str))
# def sumnum(num1 :int, num2:int ): # just for documentation purpose
#     # num1 int , num2 int
#     print(f"num1={num1}, num2= {num2}")
#     if isinstance(num1, int) and isinstance(num2 , int ):
#         res = num1 + num2
#         return res
#
#     print('--- num1 and num2 must be integer')
#
# #
# # res = sumnum("Ahmed", "Mohamed")
# # print(res)
#
#
# print(sumnum(435,45))
# print(sumnum(24,'434'))


""" functions with default argument """
# def sumnum(num1 :int, num2:int = 10 ):
#     print(f"num1={num1}, num2= {num2}")
#     res = num1 + num2
#     return res
#
#
# print(sumnum(324,5))
# print(sumnum(2))
#
# print("noha", end=' ')
# print("shehab")
#
#
# print("iti", "python", 44, sep='|')






""" function accept variable number of arguments ---> zero or more """
# print()
# print("fff")
# print("fff", "fff", "fff")


# def askforcandidates(*candidates):  # ---> * zero or more
#     print(candidates)  # accept arguments in a tuple
#
#
# askforcandidates()
# askforcandidates("dsf", "sdfsf", "sff")
# askforcandidates("werf", 3,3424,3425,True)




""" introduce yourself"""

""" functions with key value arguments """
def introduce(**info):
    print(info )


introduce(name='noha', work="iti")  # dict
introduce() # dict
introduce(fname='ahmed', lname='ali', city='cairo')






















