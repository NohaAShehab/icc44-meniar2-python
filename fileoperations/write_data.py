""" Any operations related to the files you must wrap code with try and except"""

""" 
when you try to open file with w mode --> if file doesn't exist 
python will try to create it ?
---> when you open file with w mode --> 
    file will remove old content  ---> allow writing to the file starting
    from the beginning of the file 
'"""
try:
    # 1- open the file
    filobject = open("mycv.txt", "w")
except Exception as e:
    print(f"-----{e}")
else:
    """ write data"""
    filobject.write("Hello from Ghaza \n")
    """ structure /etc/passwd ?  fname:lastname:"""
    # filobject.write("---------------------")
    filobject.writelines(["abc\n", "0439\n", "sdfsdf\n", "sfs\n"])  # iterable contains string

    filobject.close()