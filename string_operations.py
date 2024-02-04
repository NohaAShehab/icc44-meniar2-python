
"define the  string "
# message=  ""  # empty string
# message2 = 'hello from Ghaza'
#
# "1- get len of string"
# print(len(message2))
#
# """ string is treated like an array --> access string parts
# using index --> start from 0 """
# "2- slicing the string "
# print(message2[4])
#
# # print(message2[1:7])  # 1---> 6
# print(message2[::])
# # print(message2[0:])
# print(message2[::2])
# print(message2[::-1])  # reverse the string
# #
# #
# "3- count char occurrence"
# print(message2.count("a"))
# #
# """4- get index of char"""
# print(message2.index("a"))   # index return with the index of the first occurrence of the char
# #
# #
# """ operations on the string """
# "concat string "
# fname= 'noha'
# midname = 'abdelhady'
# lname= 'shehab'
# #
# fullname = fname+ "  " +midname+ "  " +lname + str \
#     (9) +"20334"  # CONCAT  available between objects from the same types
# print(fullname)
# #
# #
# """ string is immutable data """
# # lname[0]='A'  #TypeError: 'str' object does not support item assignment
#
# #
# """ formatting the string """
# #
# temp = "we have {0} students in {1} course "
# print(temp)
# no_of_students = 15
# coursename = 'python'
# res = temp.format(no_of_students, coursename)  # return new string ==> formatted according to
# print(temp)
# print(res)
#
# res = temp.format(coursename, no_of_students)  # return new string
# print(res)
#
# temp = "we have {stds} students in {crs} course "  # format using keyword
# print(temp)
# print(temp.format(crs=coursename, stds=no_of_students))
#
# print(temp.format(crs='mongo', stds=no_of_students))
#
# #
# ## f-format string
# # """ formatting string according to existing variables """
# track = 'python'
# no_of_courses = 30
# temp = f"we have {no_of_courses} courses in {track} track in menia "
# # # when you format this string--> use existing variables
# print(temp)
# #
# #
# # """ ask user enter a name  --> welcome """
# name = input("please enter your name ") # input function always returns with string
# print(name, type(name))

# welcomemessage = f"Nice to meet you {name}"
# print(welcomemessage)
#

# """===> examine string content """
# # num1 = input("enter first number")
# # num2 = input("enter second number")
# # ## check if content inside the string is number
# #
# # print(num1.isdigit())  # return True if string consists only from digits  --> (0->9)
# # # res = num1 + num2
# # # print(res)
# # if num1.isdigit() and num2.isdigit():
# #     res = int(num1) + int(num2)
# #     print(res)
# # else:
# #     print("""num1 and num2 must be integer""")
#
#
# """ isdigit() === isnumeric() ===> return True if the string consists only from digits"""
# """ examine string case """
# name = 'ahmed'
# print(name.isupper())  # True --> string consists only from upper cases char
# print(name.islower())
# print(name.istitle())    # retrun True --> each char from each word
#
#
# """ validate strings consists only from alphas [a-z]"""
# # message = input("please enter message: ")
# # # print(message.isdigit())
# # print(message.isalpha()) # return True if consists only from alphas [a-z]
#
#
# """ string consists only from spaces """
# # message = input("please enter message: ")  # input always returns with string
# # # print(message.isdigit())
# # print(message.isspace())
#
# """  change string // lower/ upper /// title// capitalize  ---> return new string """
# fullname = 'noha abdelhady shehab'
# print(fullname.upper())
# print(fullname.lower())
# print(fullname.title())
# print(fullname.capitalize())
#
# """ string interpolation"""
# fname= 'noha '
# midname= 'abdelhady '
# lname ='shehab'
# # fullname = fname  + midname + midname +lname
# fullname = fname  + midname *2 +lname
# print(fullname)
# print("iti_"*10)
#
# """ strip string """
#
# message = "nn      we love python      nn"
# print(len(message))
# print(message)
# # strip string
# # print(message.strip())  # strip spaces from the beginning and the end of the string
# # print(message.lstrip())
# # print(message.rstrip())
#
# """ strip --> strip certain chars """
# print(message.strip("nw "))  # strip n from the beginning and the end of the string
# # print(message.lstrip())
# # print(message.rstrip())
#
#
""" iterate over the string """
"""for """
# mymessage = "python is easy"
# for char in mymessage:
#     print(f"char = {char}")
#
"print char and its index "

name = 'noha'
"""
n : 0
o : 1
h:2
a: 3
"""
name = 'iti'
index = 0
for char in name:
    print(f"char = {char}, index = {index}")
    index +=1





#
# replace char by char
"replace space with underscore ? "
message = "hello from Ghaza     "
newmessage = message.replace(" ", '_')
print(newmessage)
print(message.replace("o", "@"))
newmessage = message.replace(" ", '_', 2)
print(newmessage)

#
# newmsg=mymessage.replace(" ", "_", 2)
# print(newmsg)
#
#
#
""" in operator"""
print("o" in "noha")  # return True if element in the string

#
#
# "in operator"
# print("no" in "noha")
#
#
# "noha => nh "


""" noha ? 2 """
"iti iti iti "

"noha ===> nh"