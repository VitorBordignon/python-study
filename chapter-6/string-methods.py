# in this file we going to descripe useful and common string methods and their
# results, these methods does alter the reference instead they return new values
spam = "Hello World"


def to_lower_case(string):
    return string.lower()


def to_upper_case(string):
    return string.upper()


print(f'original value ->  {spam}')
print(to_upper_case(spam))
print(f'after function run ->  {spam}')


# these following methods will return a boolean value if the string contains
# all lower or upper case chars. strings that are only numbers will always
# return false no matter which method is used

def has_lower_char(string):
    return string.islower()


def has_upper_char(string):
    return string.isupper()


print(has_lower_char(spam))
print(has_upper_char(spam))

# there are more common utilities using strings such as the the many isX()
# methods to validate strings


def is_alpha(string):
    # this will return a boolean values that will check it a the string is
    # formed only by letters
    return string.isalpha()


def is_alpha_num(string):
    # this will return a boolean values that will check it a the string is
    # formed only by letters and/or numbers
    return string.isalnum()


def is_title(string):
    # will return true if all words of the string starts with a upper case
    # char and is followed by a lower case char
    return string.istitle()


def is_space(string):
    # will return true if the string only contains whitespaces
    return string.isspace()


def is_decimal(string):
    # will return true if the string only contains numeral values
    return string.isdecimal()


def starts_with(string, substring):
    # will return true if the string only contains numeral values
    return string.startswith(substring)


def ends_with(string, substring):
    # will return true if the string only contains numeral values
    return string.endswith(substring)


def validate_user_input():
    age = None
    user_name = None

    while True:
        print('insert your age')
        user_age = input()
        if not user_age.isdecimal():
            print('please provide a number as your age')
        else:
            age = user_age
            break

    while True:
        print('insert your user name')
        user_input = input()
        if not user_input.isalnum():
            print('your user name must contain only numbers and letters')
        else:
            user_name = user_input
            break

    print(f'success, your user name is {user_name} & your age is {age}')


# validate_user_input()

# in python we can use the slipt and join methods directly on strings
def join_string(values, separator ):
    return separator.join(values)


def split_string(string, separator ):
    return string.split(separator)


# we can also partition a string in python using the partition method, this method
# will split the value before and after the separator on the string 

def partition():
    return "hello world".partition('w')
    # output -> ("hello" , "w", "orld")
    return "hello world".partition('')
    # output -> ("hell" , "o", "world")
    # you can also assign the values being returned to a specific variable
    before, sep, after = "hello world".partition(' ')

    # if the value to partition is not found the method will return a tuple where the 
    # first value is the original string, and the other values will be empty strings.


# when formatting strings we can use the following utilities

def justify_text(text, indent, fill_char = None):
    return text.rjust(indent, fill_char)
    return text.ljust(indent, fill_char)

def center_text(text, indent, fill_char = None):
    return text.center(indent, fill_char)


#these methods are specially helpful if you want to print tabular data to the stdout

def print_picnic_itens(items, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, "-"))

    for k, v in items.items():
        print(k.ljust(left_width, ".") + str(v).rjust(right_width))

eggs = {"apples": 8, "cookies": 20, "juice": 4, "honey": 2, "sandwiches": 15 }

print_picnic_itens(eggs, 12, 5)

# to remove whitespace from the left, right, and both sides of the string, we can use the 
# respective utility functions
# the strip function, without any params remove the whitespace however we can pass a string,
# value to be removed from the original string on the desired end
# ex: "SpamSpamBaconSpamEggsSpamSpam".strip("Spam") -> BaconSpamEggs

def parse_lwhitespace(string):
    return string.lstrip()

def parse_rwhitespace(string):
    return string.rstrip()

def parse_surround_whitespace(string):
    return string.strip()