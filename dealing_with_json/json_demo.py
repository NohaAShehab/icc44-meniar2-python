"""

represent data --> in json files

    file.json ---> represent data in 2 forms

    form  ---> in one json object
    {
        "data": "anvall",
        "erros" : [

        ],
        "key": {}


    }

// file array of json objects
[
    {},
    {},
    {}
]
"""
{
    "data": "anvall",
    "erros": [

    ]  # list

}  # dict


###### read data from json file

## read data - -> using builtin functions


# try:
#     fileobject = open("books.json", "r")
# except Exception as e:
#     print("Error opening file ")
# else:
#     data = fileobject.read()
#     print(data)
#     fileobject.close()



"""
[
  {"title": "book1", "pages": 10, "id": 1},
   {"title": "book2", "pages": 20, "id": 2},
   {"title": "book3", "pages": 30, "id": 3}
]
"""
# import json
#
# try:
#     fileobject = open("books.json", "r")
# except Exception as e:
#     print("Error opening file ")
# else:
#     try:
#         data = json.load(fileobject)  # return json string  in suitable format
#     except Exception as e:
#         data = []
#     else:
#         print(data, type(data))
#     fileobject.close()




# import json
#
# try:
#     fileobject = open("users.json", "r")
# except Exception as e:
#     print("Error opening file ")
# else:
#     try:
#         data = json.load(fileobject)  # return json string  in suitable format
#     except Exception as e:
#         data = {}
#     else:
#         print(data, type(data))
#     fileobject.close()




### write


import json
# def create_book():
#     title = input("please enter a book title: ")
#     try:
#         pages = int(input("please enter pages "))
#     except Exception as e:
#         pages = 0
#
#     book = {'title': title, 'pages': pages}
#
#     ### saving in the file
#     try:
#         filobject=  open("books.json", "a")  # keep old content
#     except Exception as e:
#         print(e)
#
#     else:
#         json.dump(book, filobject)
#
#
# create_book()






""" save data in json 

    --> read old data  --> in a list 
    ---> add dict to the list 
    ---> write the list 

"""

# from json_operations import read_data_from_json


# def create_book():
#     title = input("please enter a book title: ")
#     try:
#         pages = int(input("please enter pages "))
#     except Exception as e:
#         pages = 0
#
#     book = {'title': title, 'pages': pages}
#     old_data = read_data_from_json("books.json")  # list
#     print(old_data)
#     old_data.append(book)
#     ### saving in the file
#     try:
#         filobject=  open("books.json", "w")  # keep old content
#     except Exception as e:
#         print(e)
#
#     else:
#         json.dump(old_data, filobject, indent=2)
#
#
# create_book()


""" optimized code """
from json_operations import read_data_from_json, write_data_to_json
from inputs_module import  ask_for_int

def create_book():
    title = input("please enter a book title: ")
    pages = ask_for_int("please enter no of pages ")
    book = {'title': title, 'pages': pages}
    old_data = read_data_from_json("books.json")  # list
    print(old_data)
    old_data.append(book)
    ### saving in the file
    saved = write_data_to_json("books.json", old_data)
    if saved :
        print('---- book saved successfully----')



create_book()




