import time, sys

height = 12
try:
    while True:
        for i in range(1, height):
            time.sleep(0.1)
            print("#" * i, " " * (height - i))
        for i in range(height, 1, -1):
            time.sleep(0.1)
            print("#" * i, " " * (height - i))
except KeyboardInterrupt:
    sys.exit()
