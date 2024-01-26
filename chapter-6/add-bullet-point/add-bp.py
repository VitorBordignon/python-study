#! python3

# add-bp.py -> adds a bullet point to the begging of every text on your system clipboard
# and them replaces the original values with the parsed ones 
import pyperclip


def display_usage():
    print('add-bp.py -> adds a bullet point to the begging of every text on your system clipboard')
    print('''
        Usage: Your system clipboard should contain text to be formatted, example
            List of animals
            List of fruits
            List of places to travel
            List of most beautiful places 
        ''')

def __init__():

    values_to_parse = pyperclip.paste().split('\n')

    for i in range(len(values_to_parse)):
        values_to_parse[i] = values_to_parse[i].strip()
        values_to_parse[i] = "* " + values_to_parse[i]
    
    pyperclip.copy('\n'.join(values_to_parse))

    print('Formatted values copied to system clipboard')

__init__()



    







