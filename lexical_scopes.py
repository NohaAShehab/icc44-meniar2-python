""" scoping of functions """
""" variable defined inside the python file --> variable with global scope 
can be accessed anywhere in the script 
"""
# course = 'python'  # python file
# print(course)
# course = 'Python Programming'
# print(course)
#
# """ print global variable from inside the function """
#
#
# # def printCourseInfo():
# #     print(f"course = {course} from the printcourseinfo function")
#
#
# # printCourseInfo()
#
# """ variable defined inside function """
#
# def sumnum(num1, num2):
#     """ res is variable defined inside the function"""
#     res = num1 + num2  # res is variable with local scope
#     print(f"res = {res}")
#     return res
#
# sumnum(4,5)
# # print(res)  ### NameError: name 'res' is not defined


"""  modify global variable from inside the function """

# course = 'python'
# print(f"course = {course}")

# def modify_course():
#     course = 'Python Programming'  # create new local variable
#     print(f"from inside the function {course}")
#
# modify_course()
# print(f"after modifying the global variable :{course}")


""" modify the global"""
# course = 'python'
# print(f"course = {course}")
#
# def modify_course():
#     global course  # please use the global variable and don't create new local
#     course = 'Python Programming'
#     print(f"from inside the function {course}")
#
# modify_course()
# print(f"after modifying the global variable :{course}")






""" function inside a function """


# def outerfunction():
#     """ local variable can be accessed anywhere in the function (inner_function )"""
#     username = 'iti'   # local variable ==> can be accessed only inside the function
#
#     # define function inside a function
#     def printUsername():
#
#         print(f"username= {username} ===> from inside  printusername")
#
#
#
#     printUsername()
#
#     print(f"username = {username}")
#
#
# outerfunction()


""" modify the local variable from inside inner function """

# def outerfunction():
#     """ local variable can be accessed anywhere in the function (inner_function )"""
#     username = 'iti'   # local variable ==> can be accessed only inside the function
#     # define function inside a function
#     def printUsername():
#
#         print(f"username= {username} ===> from inside  printusername")
#     printUsername()
#
#     def modifyUsername():
#         username = input("please enter username ")   # create new local variable
#         print(f" updated username= {username}")
#
#     modifyUsername()
#     print(f"username = {username}")
#
#
# outerfunction()

def outerfunction():
    """ local variable can be accessed anywhere in the function (inner_function )"""
    username = 'iti'   # local variable ==> can be accessed only inside the function
    # define function inside a function
    def printUsername():

        print(f"username= {username} ===> from inside  printusername")
    printUsername()

    def modifyUsername():
        nonlocal username   # username is nonlocal ---> use the parent  username variable
        username = input("please enter username ")   # create new local variable
        print(f" updated username= {username}")

    modifyUsername()
    print(f"username = {username}")


outerfunction()















