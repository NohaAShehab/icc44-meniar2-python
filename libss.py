
"1- os "

import os

# print(os.getcwd())
# print(os.getlogin())
# print(os.getgid())
# print(os.getenv("SHELL"))
#
# ## linux command
# # os.mkdir("oop")  # FileExistsError
# os.system("touch abc")   # pure linux command
#
# os.system("ls -l")

# os.system("systemctl status apache2")

# os.system("sudo systemctl start apache2")

#########################################################
# import datetime
#
# print(datetime.datetime.now())  # current date // time according to os
#
# import time
# print(time.time())  # return time ---> in timestamp format
# print(round(time.time()))
# ## use it as id
#
# # def generate_id():
# #     return round(time.time())
# import datetime
# ### "validate time 0> valid"


""" import math """
import math

print(math.pi)

print(math.ceil(44.66))
print(math.ceil(44.33))

""" random """
# import random
# print(random.random())  # 0 ---> 1 --> float number
#
# # generate id random
# num  =random.randint(1,100000)
# print(num)


""" re """

## uuid -->
# import uuid
#
# print(uuid.uuid1())  # generate id -->

""" regular expressions """

""" --> validate if string  --> follow specific pattern """

"""
    email ----> valid ---> rules ==> @ , .. , 
    password ---> 
        mix number char , up down, special char 
    --> phone numbers   {01}// === > 11 number 
"""

import re

# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#
# email = input("please enter your email: ")



""" match  ---> return match object if the first part of the string follows the patter """
# res = re.match(regex, email)  # match object ? None

# print(res)
# if res :
#     print("--- email is valid")
# else:
#     print("--- email is not valid")

# res = re.fullmatch(regex, email)  # make sure that all the string parts follows the pattern
# print(res)
# if res :
#     print("--- email is valid")
# else:
#     print("--- email is not valid")


## search
pattern = r'/iI/'
print(re.search(pattern, "it iI "))



print(re.match("c", "abcdef") )   # No match
# res = re.search("c", "abcdef  abcd ")  # Match
#
# print(res)

res = re.findall("c", "abcdef  abcd ")  # Match
print(res)




