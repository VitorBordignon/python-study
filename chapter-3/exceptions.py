def spam(divideBy):
    return 42 / divideBy


print(spam(2))
print(spam(10))
# print(spam(0))


def spamCatch(divideBy):
    try:
        return 42 / divideBy
    except Exception:
        print(Exception)
        print("Exception caught")
        print("Invalid value")


spamCatch(2)
spamCatch(10)
spamCatch(0)
