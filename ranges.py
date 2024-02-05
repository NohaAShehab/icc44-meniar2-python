

""" generate sequence of numbers ---> """

myrange = range(10)  # start 0 , stop= 10 , step
print(myrange)

# for num in myrange:
#     print(f"num = {num}")


myrange2 = range(1, 10 , 2)  # range(start, stop, step)
print(myrange2)

# for num in myrange2:
#     print(f" num = {num}")

""" cast range to list """
myr = list(myrange2)
print(myr)

""" ascending range ? """
myr2 = range(10, 1 , -1)
print(myr2)
print(list(myr2))