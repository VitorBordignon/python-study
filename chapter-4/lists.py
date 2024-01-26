import random
##### LISTS #####

## Lists and tuples as almost identical to basic arrays 
default_list = []

integer_list = [1,2,3,4,5]

string_list = ["foo", "bar"]

mixed_values_array = [1,2, "value", True]

## Access a unexistent index position will throw an error, the same goes to trying to idx 
# with a float -> invalidAccess = list[1.2]
invalid_idx_access = string_list[32]

## Negative values can be use as index, they represent de reverse look of an list, -1 is 
## the last element, -2 second last and so on. 
reversed_access = string_list[-1]

## Python has a feature almost identical to array.slice on js.
## ** Remember that the last goes to but does no include the end position **
sliced_values = integer_list[0:3]

## We can omit values from both sides of the operation, these omits means respectively: 
# the begging and end of list
sliced2 = integer_list[:2]
sliced3 = integer_list[1:]

##########################################################################################

## Get the length of a list with the built-in len() function ( works with strings as well )
def list_or_string_length(list_or_string_value):
    return len(list_or_string_value)


## Lists can be operated with concatenation and multiplication
def concat_lists(list_1, list_2):
    return list_1 + list_2
## Output: [list_1 + list_2]

def multiply_lists(list, amount):
    return list * amount
## Output: [1,2,3,4] * 2 => [1,2,3,4,1,2,3,4]


## Deletes an element from a list and shift the indexes
def remove_from_list(list, idx):
    del list[idx]
    return;

# Exercise 1
def store_names():
    names = [];
    while True:
        print('Enter a cat name, (or enter nothing to quit): ')

        name = input();

        if name == '':
            break;
            
        names = names + [name] # list concatenation
    
    print('the names are:')

    for name in names:
        print(" " + name)

    return;

## Iterate over lists
def iterate(list):
    for i in range(len(list)):
        print(i)

## check if a value is in a list 
def is_value_on_list(list, value):
    return value in list
    ## we can invert this condition by
    return value not in list

# we can fetch values from a list with the following syntax
def extract_list_values_to_var(list):
    ## the number of variables to unpack must be the equal to the length of the list,
    ## otherwise a error will be thrown
    value1, value2, value3 = list
    print(value1, value2, value3)
    return;

# we can use the enumerate function to iterate over the keys of a list
# the enumerate function returns two values, the index and the item itself
def enumerate_iterable():
    supplies = ["wood", "iron", "copper", "steel"]

    for index, item in enumerate(supplies):
        print('index' + str(index) + "contains the supply: " + item)

    return

## using the built in random package we can sort and pick an item of a list randomly
## the shuffle method will modify the original array, not create a copy
def randomize_list(list, option):
    if option == 'pick':
        random.choice(list)
    elif option == 'shuffle':
        random.shuffle(list)
    return

##### DEFAULT LIST METHODS #####

##list.index -> returns the index of the first occurrence of value on a list  
## throws exception otherwise
def index_of(list, value):
    return list.index(value)

## insert the value on a list on a specific index
def insert_values(value, list, index):
    return list.insert(index, value)

## insert the value at the end 
def append_value(value, list, index):
    return list.append(index, value)

## remove the value from a list, if the value is not found, throw an exception.
## if there are multiple occurrences of the value, remove the first one that is found.
def remove_value(value, list):
    return list.remove(value)

## sort strings bt ASCII (this means uppercase letters come first, 
## ex: "Alice", "Bob", "ana", "carol") order or integers from lowest to highest
## however, it will throw an error if a list contains strings and ints to be sorted
def sort_list(list):
    list.sort()
    return

    ## we can reverse the order of sorting by passing an argument to the sort function
    list.sort(reverse=True)
    return 

    ## to sort alphabetically, pass a function to be used on each element of the list
    list.sort(key=str.lower)
    return 


## reverse the elements of a list
def reverse_list(list):
    list.reverse()
    return;
