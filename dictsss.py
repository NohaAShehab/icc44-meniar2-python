info = ["noha", 31, "iti", "python", 44]

""" represent labeled data """

""" dict 

    key:value
"""

""" data represented inform of key value pair 
    dict ---> doesn't allow key duplication ---> set
    --> used in representing labeled data 
"""
""" python 3.7 --> dict ordered in memory """

"""define dict """
d = {}
myd = dict()
myinfo = {"name": "noha", "work": "iti", "city": "cairo", "age": 31, "name": "Noha Shehab"}
print(myinfo)
""" get len """
print(len(myinfo))
""" dict is mutable data ---> key value pair  --> key : string """
myinfo["work"] = "Information Technology Institute"  # updated existing key
print(myinfo)

myinfo["salary"] =10000  # if key not exists --> add it to the dict

""" access elements  --> key """
print(myinfo["work"])
""" check if element exists in dict """
print("cairo" in myinfo)  # false
""" when you use in operator  --> check if value exists in keys """
print("city" in myinfo)

""" get dict keys, values , value pairs  """
keys  = myinfo.keys()  # return with dict keys
print(keys, type(keys))
keys_list = list(keys)
print(keys_list)

## get values

values = myinfo.values()
print(values, type(values))  # dict_values
values_list = list(values)
print(values_list)

print("cairo" in myinfo.values())
"for loop "
# for abbass in myinfo:  # abbass  -> represent key
#     print(f"{abbass}")


for key in myinfo:  # abbass  -> represent key
    print(f"Key= {key}, value = {myinfo[key]}")

# for key , value in myinfo:  # abbass  -> represent key
#     print(f"Key= {key}, value = {value}")


""" dict items """

d_items = myinfo.items()  # dict_items --> represent each key:Value 000> inform of tuple
print(d_items)
# you can cast dict_items to list
items_list = list(d_items)
for k , v in myinfo.items():
    print(f"key={k}, value={v}")

'remove element from dict '
"""1- pop ---> using key """
city_info = myinfo.pop("city")  # pop key:value from dict ---> return popped value
print(city_info)
print(myinfo)

"del"
#
del myinfo["age"]
""" clear dictionary """

# myinfo.clear() ## remove all key_value pairs 000> remaining 0--> empty dict

""" empty dict , tuple, set , list ---> represent falsy values."""
"update"
info = {"name":"test", "track":"test"}
add_info  = {"name":"updated", "location":'cairo', "intake":44}
info.update(add_info)
""" if key exists --> update its --> if not exists --> add key:value"""
print(info)


# print(myinfo)
# import sys
# print(sys.getsizeof(myinfo))

# """"""
# myinfo.clear()
# print(sys.getsizeof(myinfo))




#######################################
