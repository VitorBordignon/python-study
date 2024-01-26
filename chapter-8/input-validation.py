import pyinputplus as inputp

# Basic input validation with python


# the method below is a simple example of input cli validation. this loop will not break
# until  the value on the stdin is a number that can be converted string
def init_1():
    while True:
        print("Enter your age:")

        age = input()

        try:
            age = int(age)
        except:
            print("Please use numeric digits.")
            continue

        if age < 1:
            print("Please enter a positive number.")
            continue

        break

    print(f"Your age is {age}")
    return


# The package PyInputPlus provides a nice implementation of the input() built in method
# It contains a lot of pre built methods for all types of cli user input
# Those methods contains attributes that can configure the behavior of the method


def sandbox():
    inputp.inputStr()

    # Ensures the user enters one of the provided choices
    inputp.inputChoice()

    inputp.inputNum()

    inputp.inputDatetime()
    # validates email address
    inputp.inputEmail()
    ## display sensitive information as a ********
    inputp.inputPassword()
