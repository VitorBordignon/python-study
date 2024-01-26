import sys, time

indent = 20

identDecreasing = True

try:
    while True:
        print(" " * indent, end="")
        print("***********")
        time.sleep(0.1)
        if identDecreasing:
            indent = indent - 1
            if indent == 0:
                identDecreasing = False
        else:
            indent = indent + 1
            if indent == 20:
                identDecreasing = True
except KeyboardInterrupt:
    sys.exit
