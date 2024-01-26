# Dictionaries are the data structure in python that allow us to store
# key value pairs

# The keys can be strings or number

# Dictrionaries differ from lists in the sense that they are unordered
# key values and this matter in equallity comparations

# [1,2,3,4] == [1,2,4,3] false

# {"prop1": 1, "prop2": 2 } == {"prop2": 2, "prop1": 1 } true


base_input = {"prop1": 1, "prop2": 2, "prop3": 3}


def log_dict_values():
    for value in base_input.values():
        print("value " + str(value))
    return


log_dict_values()


def log_dict_keys():
    for key in base_input.keys():
        print("key: " + key)
    return


log_dict_keys()


def log_dict_items():
    for key_value_pair in base_input.items():
        print(key_value_pair)
    return


log_dict_items()


# validate if a key exists on a dict

def is_key_in_dict(key):
    return key in base_input


print(is_key_in_dict("prop1"))
print(is_key_in_dict("prop5"))


# fetch the value of a key in a dict

def get_value(key):
    # the second argument of the get function is a fallback value in the case
    # the key does not exist
    return base_input.get(key, 0)


# set the default value to use on key if there is none

def set_default():
    # if the key exists on the dict, returns the current value of the key
    return base_input.setdefault("prop4", "4")


# use set default to group the letters of a string


def count_letter():
    base_value = "It was a bright cold day in April, and the clocks were striking thirteen."
    count = {}

    for char in base_value:
        count.setdefault(char, 0)
        count[char] = count[char] + 1

    print(count)


count_letter()

