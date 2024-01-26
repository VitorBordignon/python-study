spam = ["apples", "bananas", "tofu", "cats", "elephant"]

def join_list(list_value, separator):
    if(len(list_value) == 0):
        return " "

    list_value[-1] = "and " + str(list_value[-1])
    
    response = ''

    for idx, value in enumerate(list_value):
        if idx == len(list_value) - 1:
            response += value
            continue

        response += str(value) + separator
    
    print(response)

    return response;

join_list(spam, ", ")