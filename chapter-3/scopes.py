def spam():
    print(eggs)


eggs = 1
# spam()


# def local():
#     spam()
#     bacon = 1

#     def ham():
#         bacon = 2
#         print(bacon)

#     ham()
#     print(bacon)


# local()


# Access variables from the global scope with the global keyword
def imp():
    global eggs
    eggs = 123


spam()
imp()
spam()
