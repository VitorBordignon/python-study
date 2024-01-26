import time


def collatz(num):
    while num >= 1:
        time.sleep(0.1)

        if num % 2 == 0:
            num = num // 2
            print(num)
        elif num % 2 == 1:
            num = num * 3 + 1
            print(num)

        if num == 1:
            break
    return


collatz(1)
