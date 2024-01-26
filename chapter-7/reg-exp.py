import re

# we are checking for the american pattern xxx-xxx-xxxx


def is_phone_string(value):
    # check the length of the value
    if len(value) != 12:
        return False

    for i in range(0, 3):
        if not value[i].isdecimal():
            return False

    if value[3] != "-":
        return False

    for i in range(4, 7):
        if not value[i].isdecimal():
            return False

    if value[7] != "-":
        return False

    for i in range(8, 12):
        if not value[i].isdecimal():
            return False

    return True


def find_phone_on_string(string):
    for i in len(string):
        chunk = string[i : 12 + i]
        if is_phone_string(chunk):
            print("phone found:", chunk)

    print("done")


# the approach above is very simple and error prone, we could solve it more
# simply with regex


def find_with_regex(string):
    # just check if the string is composed of xxx-xxx-xxxx while x are
    # all numbers. this compile method is just a regxer builder obj
    # where we can call methods to check if a string matches this pattern
    matcher = re.compile(r"\d\d\d\-\d\d\d-\d\d\d\d")

    is_phone = matcher.search(string)

    if is_phone is not None:
        # if matcher does not return none, it returns a Match Object which has
        # a few methods to work with capture groups
        print("Phone number found: ", is_phone.group())
        print("Done")
        return

    print("Not a phone number, exiting")


def find_using_capture_groups(string):
    matcher = re.compile(r"(\d\d\d\)-(\d\d\d)-(\d\d\d\d)")

    # we could also capture this way, isolation the area code from the phone
    # number
    # matcher_2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

    is_phone = matcher.search(string)

    if is_phone is not None:
        # if matcher does not return none, it returns a Match Object which has
        # a few methods to work with capture groups
        print("Phone number found: ", is_phone.group())
        print("Done")

        print("groups")
        print(is_phone.group(1), is_phone.group(1), is_phone.group(2))

        print("all groups")
        print(is_phone.groups())
        return

    print("Not a phone number, exiting")


# we can use OR operations or regex with pipes, it will return on the first
# truthy match
def find_using_pipes():
    string = "Batmobile lost a whell, but Batman is ok"

    regex = re.compile(r"Bat(man|mobile|copter|bat)")

    regex.search(string)

    # will return only the string Batmobile
    print(regex.group())


# we can use the ? operator to indicate a optional value to match, it will
# match one or none occurrences during the text.


def find_using_question_mark():
    string = "Batwoman is ok"
    string2 = "Batman is ok"

    regex = re.compile(r"Bat(wo)?man")

    match1 = regex.search(string)
    match2 = regex.search(string2)

    # output -> Batwoman
    print(match1.group())
    # output -> Batman
    print(match2.group())

    # output -> Batwoman
    print(match1.groups())


# we can use the * operator to match zero or more of the group that precedes
# the operator on the regex pattern


def find_using_star_operator():
    string = "Batwoman is ok"
    string2 = "The Adventures of Batwowowowoman"

    regex = re.compile(r"Bat(wo)*man")

    match1 = regex.search(string)
    match2 = regex.search(string2)

    # output -> Batwoman
    print(match1.group())
    # output -> Batman
    print(match2.group())

    # output -> Batman
    print(match1)
    return


a = 1


# In python regex matches are greedy by default, meaning that they will always match
# the bigger string if finds more than one occurrence, we could change this behavior
def greedy_match():
    string = "HaHaHaHaHa"

    greedy_match = re.compile(r"(Ha){3,5}")

    greedy_match.search(string)
    # Output -> "HaHaHaHaHa" even if HaHaHa was captured first

    greedy_match.search(string)
    # Output -> "HaHaHaHaHa" even if HaHaHa was captured first

    # this means that, in python the ? operator for regex have two different, unrelated
    # functionalities
    lazy_match = re.compile(r"(Ha){3,5}?")
    lazy_match.search(string)
    # Output -> "HaHaHa" because its stops matching after the first occurrence

    # alternatively we could use another method to get all the occurrences of pattern on a string
    # .search() returns the first match
    # .findall() returns the first match

    lazy_match.findall(string)

    # returns both of the matching results "HaHaHa" and "HaHaHaHaHa"


def custom_classes():
    # sometimes the shorthands like: \w, \s \d are too broad and we want to narrow it down
    # we can use [] to define such narrowing

    # matches uppercase and lowercase letters and numbers
    match = re.compile(r"[a-zA-z0-9]")

    # matches only vowels
    another_match = re.compile(r"[aeiouAEIOU]")

    # we can negate groups as well. this now will only match the consonants
    negation_match = re.compile(r"[^aeiouAEIOU]")

    # we can use the ^ narrow the pattern to the begging of a string
    strict_match = re.compile(r"^Hello")

    # we can use the $ narrow the pattern to the end of a string
    strict_match = re.compile(r"World$")


def extra_params():
    # we can add the global flags to our pattern in the compile function
    insensitive_match = re.compile(r"\w", re.I)

    # makes the dot operator match new lines as well
    buff_dot = re.compile(r".*", re.DOTALL)

    combined = re.compile(r".*", re.DOTALL | re.I | re.VERBOSE | re.MULTILINE)


def sub():
    # we can use the pattern to substitute values on a string as well

    match = re.compile(r"Agent \w+")

    sub_string = match.sub(
        "CENSORED", "Agent Alice gave the secret documents to Agent Bob."
    )
    # OUTPUT -> 'CENSORED gave the secret documents to CENSORED.'
    # works like .replaceAll in javascript but we declare the pattern and then call the function
    # with the values to replace and the target string instead of
    #   let randomString = "123456123"
    #   randomString = randomString.replaceAll(/.*/, "")
