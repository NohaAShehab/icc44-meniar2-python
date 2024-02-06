
""" every python file (.py) is considered to be a module"""
def ask_for_int(message):
    while True:
        num = input(message)
        if num.isdigit():
            return  int(num)

        print("==== please enter valid number =====")



print(ask_for_int("please enter salary"))