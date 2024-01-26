import random
import sys


# while True:
#     print("Type exit to exit the program:")
#     res = input()
#     if res == "exit":
#         sys.exit()

#     print("You typed " + res + ".")


# while True:
#     num = 16
#     print("I`m thinking about a number, take a guess")

#     guess = int(input())

#     if guess < 16:
#         print("Too low")
#     elif guess > 16:
#         print("Too high")
#     elif guess == 16:
#         print("Correct")


# rndNum = random.randint(1, 20)

# print("I'm thinking about a number between 1 and 20, take a guess:")

# # Give the player 6 attempts
# for guesses in range(1, 7):
#     guess = int(input())

#     if guess < rndNum:
#         print("Too low")
#     elif guess > rndNum:
#         print("Too high")
#     else:
#         break

# if guess == rndNum:
#     print("Good job! You guessed in " + str(guesses) + " attempts")
# else:
#     print("Nope, i was thinking of number: " + str(rndNum))

for i in range(1, 23, 3):
    print(str(i))
