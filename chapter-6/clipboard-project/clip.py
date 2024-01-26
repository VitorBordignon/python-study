#! python3
import sys
import pyperclip


responses = {
    "busy": """Sorry, can we do this later this or next week?""",
    "agree": """Yes, I Agree. Sounds fine to me""",
    "upsell": """Would you consider make this a monthly donation?"""
}

# second command line argument is the message we want to return 
# (the first one is the path of the file)

def display_usage():
    print("Usage: [keyword] -> copies the phrase associated with the value.")

    print("Possible Values:")

    for i in responses.keys():
        print(i.rjust(len(i) + 1, "-"))

    print("Please, try again")


def __init__():

    if len(sys.argv) < 2:
        display_usage()

    keyword = sys.argv[1]

    if keyword.lower() not in responses.keys():
        display_usage()
    else:
        pyperclip.copy(responses[keyword])
        print('Chosen message copied to the clipboard')

    return 0;

__init__()


