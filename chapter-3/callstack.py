# Basic representation of a call stack
def a():
    print("a() starts")
    b()
    d()
    print("a() return")


def b():
    print("b() starts")
    c()
    print("b() return")


def c():
    print("c() starts")
    print("c() return")


def d():
    print("d() starts")
    print("d() return")


a()
