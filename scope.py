# global scope
# name = "Dave"

# def greeting():
#     print(name)
# greeting()        here the name is passed as the global scope so it is printing dave


# def greeting():
#     color="blue"
#     print(name)
# greeting()
# print(color)      here it will give error as the name color is defined in the local variable and asked in outside the function.

# def greeting():
#     color = "blue"
#     print(color)
#     print(name)

# greeting()        here the name and as weelll as the color will get print sucessfully


# def greeting(name):
#     color = "blue"
#     print(color)
#     print(name)

# greeting("John")  # here the name is pass as a aparameter to the function


# def another():
#     greeting("Dave")

# another()
# so here the function greeting is a global scope so it can be called and define in local scope of the another function


# global keyword
# here if we not use global keyword then it will not considered the value of const key declare in globaly
# name = "Dave"
# count = 1


# def another():
#     color = "blue"
#     global count
#     count += 1
#     print(count)

#     def greeting(name):
#         print(color)
#         print(name)
#     greeting("Ashu")


# another()


import sys
import random
from enum import Enum

game_count = 0


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input(
        "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    print("Python chose " + str(RPS(computer)
                                ).replace('RPS.', '').title() + ".\n")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            return "🎉 You win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            return "🐍 Python wins!"

    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print("\nGame count: " + str(game_count))

    print("\nPlay again?")

    while True:
        playagain = input("\nY for Yes or \nQ to Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")


play_rps()
