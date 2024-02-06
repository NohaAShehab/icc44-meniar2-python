import json
def read_data_from_json(filename):
    try:
        fileobject = open(filename, "r")
    except Exception as e:
        print("Error opening file ")
    else:
        try:
            data = json.load(fileobject)
        except Exception as e:
            data = []
        else:
            print(data, type(data))
        fileobject.close()

        return data


def write_data_to_json(filename, data:list ):
    try:
        filobject=  open(filename, "w")  # keep old content
    except Exception as e:
        print(e)
        return  False

    else:
        json.dump(data, filobject, indent=2)
        return  True
