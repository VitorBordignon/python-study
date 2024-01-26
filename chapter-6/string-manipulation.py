# in this section we going to explore ways to manipulate a string using python


# concatenate two strings
def concat(value_1, value_2):
    print(value_1 + value_2)
    return value_1 + value_2

# to use quotes inside a string, in python we must use the double quotes
# 'this is Alice's bear ' -> this errors
# "this is Alice's bear"  -> works fine.

# We can use the backslash character to escape chars that would be invalid
# inside the string


escaped_string = 'this is Alice\'s bear'

# Examples of escaped chars

# \' single quite
# \" double quote
# \n new line
# \t tab
# \\ backslash


# In python we have the concept of a raw string which means we can tell the
# language the string being passed must be interpreted as a raw string
# instead of a escaped char we must use the r operator to tell python it's
# a raw string

print('the following print will not contain escaped chars')
print(r'this is Alice\'s bear')

# raw string are very useful when dealing with string with special characters
# such as paths with backslashes (c:Windows/User/Desktop/folder/file)

# while we can use the \n to create a new line, when dealing with multiline
# strings it's best to use the proper syntax for multiline strings in python
# which is the triple single quotes '''string'''. On multiple lines
# special chars does not need to be escaped


print('''
      Alice is a very
      intelligent lady
      and has a very beautiful dog
      named Marshall
      ''')

'''multiline strings are also often used for documentation'''

# Since strings are indexed in python we case use the common syntax of slicing
# lists on strings, this also does not alter the reference, instead creates
# a new value

spam = 'hello world'

bar = spam[0:5]

print(bar)


# we can also use the in and not in operators to find if a substring is present
# inside another string

def is_value_on_string(sub, string):
    return sub in string

    # return sub not in string


# until now we have been using the add operator (+)  to join strings, however
# this is not the most optimal way of executing this types of common operations
# instead we can use the interpolation operator to modify strings


def interpolate_values():
    name = "George"
    age = 15
    print('%s is %s years old' % (name, age))


interpolate_values()

# the example bellow is only available in python 3.6^

def interpolate_v2():
    name = "George"
    age = 15
    print(f'{name} is {age} years old')

interpolate_v2()
