
""" import module that contains the function """
# import inputs_module
# def calculator():
#     num1 = inputs_module.ask_for_int("please enter first number ")
#     num2 = inputs_module.ask_for_int("please enter second number ")
#     res = num1 + num2
#     print(f"the result = {res}")
#
# calculator()

""" alias module """

# import inputs_module as myinput
# def calculator():
#     num1 = myinput.ask_for_int("please enter first number ")
#     num2 = myinput.ask_for_int("please enter second number ")
#     res = num1 + num2
#     print(f"the result = {res}")
#
# calculator()

""" import part of the module """
#
# from inputs_module import  ask_for_int
#
# print(ask_for_int("please enter day: "))

""" alias imported function """
# from inputs_module import  ask_for_int as getnumber
#
# print(getnumber("please enter a num : "))


""" ---> import module from package """
#
# import iti.greetingModule
#
# iti.greetingModule.sayHello("Ahmed")


""" alais"""
# import iti.greetingModule as mm
# mm.sayHello("Ahmed")


# """ import part of the module """
# from iti.greetingModule import sayHello
#
# sayHello("Ali")


import menia_track
menia_track.saywelcome("Ali")

# from menia_track.validation_module import validate_number
# print(validate_number(48734.43))


print(menia_track.validate_number(3434.434))





















