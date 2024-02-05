
""" use while loop --> unknown number of iterations """

# count = 0
# while count < 5:  # based on condition code inside while --> executed
#     print(f"count = {count}")
#     count +=1

""" break , continue --> used with loops only 

    break  ---> break the loop 
    continue ---> skip current iteration and continue to the next 
"""

# for i in range(10):
#     if i==5:
#         break  # break the loop
#     print(f"i = {i}")
#
# print("--- after the loop ")


# for i in range(10):
#     if i==5:
#         break  # break the loop
#     else:
#         print(f"i = {i}")
#
# print("--- after the loop ")



""" continue """
for i in range(10):
    if i==5:
        continue  # continue to the next iteration
    print(f"i = {i}")


print("--- after the loop ")

""" -------------------------------------------------------------- """

""" break , continue --> used with loops for , while """

# while True:
#     name = input("Enter your name: ")
#     # name-> consists  ---> alphas
#     if name.isalpha():
#         break
#
# print(f"name = {name}")


# name = input("please enter your name: ")
# while not name.isalpha():
#     name = input("please enter your name: ")
#
# print(f"name = {name}")


""" ----> """

# for i in range(5):
#     if  i==3:
#         break
#     print(f"i = {i}")
# else:
#     """ this block will be executed when loop reached its end """
#     print('----- loop reached its end ----')
#
#
# print('----- after the loop ')
#


for i in range(5):
    if  i==3:
        continue
    print(f"i = {i}")
else:
    """ this block will be executed when loop reached its end """
    print('----- loop reached its end ----')


print('----- after the loop ')


""" --->using for loop:  do action if loop reached its end  ---> for else """























