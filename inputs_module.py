
""" every python file (.py) is considered to be a module"""
def ask_for_int(message):
    while True:
        num = input(message)
        if num.isdigit():
            return  int(num)

        print("==== please enter valid number =====")

""" each python module =-> has entry point for the run --> __name__=='__main__'
when run the module -->  use this main 
"""
### __name__ = '__main__'
if __name__ == "__main__":
    # this line will be called only if input_module run
    print(ask_for_int("please enter salary"))

""" some parts must be run only when this file called from run"""