""" errors

logical error
"""


# def sumnum(num1, num2):
#     res = num1 * num2
#     return res
#
#
# print(sumnum(2, 2))
#
# print(sumnum(3, 4))  # logic


"do test my own ---> "
### 2 ways --> developer  ---> unit tests  ---> code ---> unit testing
## before program ---> inputs - -> expected output  ---> pass all tests



def sumnum(num1, num2):
    res = num1 + num2
    return res


# print(sumnum(2, 2))
# print(sumnum("ahmed", "Ahmed"))   # do tests ---> cover all cases

""" runtime errors """

#
# num = int(input("please enter a number : "))
# print(num)


# print(name)  # NameError: name 'name' is not defined


""" """
# num1 = 10
# num2 = 0
# print(num1/num2)   # zeroDivisionError


""" Exception handling  ---> Plan b  """
# num = int(input("Enter a number: "))
# try:
#     # num = int(input("Enter a number: "))  # may be input alpahstring
#     """ NEVER TRUST USER INPUT """
#     print(45/0)
# except:
#     print("---- problem happened")


# print('-------------------------------')

""" define exception causes // exception description  """
# try:
#     num = int(input("Enter a number: "))  # may be input alpahstring
#     """ NEVER TRUST USER INPUT """
#     print(45/0)
# except Exception as abbass :
#     print(f"---- problem happened : {abbass}")
#


""" action ----"""

# try:
#     num = int(input("Enter a number: "))  # may be input alpahstring
#     """ NEVER TRUST USER INPUT """
# except Exception as abbass:
#     print(f"---- problem happened : {abbass}")
#     num= 1
#
#
# print(num*10)



# try:
#     num = int(input("Enter a number: "))  # may be input alpahstring
#     """ NEVER TRUST USER INPUT """
#     print(name)
#
# except TypeError as te:
#     print(f"----> {te}")
# except ZeroDivisionError as ze:
#     print("-=== zero division error -===")
# except NameError as ne :
#     print(ne )
#     name = ''
# except Exception as e:
#     print(e)
#     num = 0



""" else: """
# try:
#     num = int(input("Enter a number: "))  # may be input alpahstring
#     """ NEVER TRUST USER INPUT """
# except Exception as e:
#     print(e)
# else:
#     """ this block will be executed if no problem happened """
#     num = num * 10
#     print(num)
# finally:
#     print("==== this line will be executed always ")
#
# print("--------------------------------------------------")








# try and except and finally

# def askforInt():
#     try:
#         num = int(input("please enter a number: "))
#     except Exception as e:
#         return False
#     else:
#         return num
#     finally:
#         ### preceeds the return
#         print("-====== the function executed successfully ! =====")
#
# print(askforInt())
#
#



# def sumnum(num1, num2):
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 + num2
#         return  res
#     # print("num1 and num2 must be integers")
#     raise ValueError("num1 and num2 are not integers")


# print(sumnum(4,"jkhjkh"))
# print("323" +232)
#####



from inputs_module import  ask_for_int
def divnums():
    num1 = ask_for_int("please enter first number")
    num2 = ask_for_int("please enter second number")
    if num2==0:
        raise ZeroDivisionError("num2 must not be zero")
    print(f"num1 = {num1}, num2 = {num2}")
    res = num1 / num2
    return res

print(divnums())






