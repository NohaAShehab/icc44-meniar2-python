""" Any operations related to the files you must wrap code with try and except"""
""" open file for read
 read file content 
 
 ---."""

try:
    # 1- open the file
    filobject = open("students.txt", "r")
except Exception as e:
    print(f"-----{e}")
else:
    print(filobject)
    "## read the data"
    filedata = filobject.read()  # read file content into one string
    print(type(filedata))
    print(filedata)
    """ read file line by line """
    filobject.seek(0)
    lines  = filobject.readlines()  # read file content into one list
    print(lines)
    """"""
    # lines = []
    # for l in filobject:  # reference to the file
    #     lines.append(l)
    # print(lines)


    # close the file
    filobject.close()