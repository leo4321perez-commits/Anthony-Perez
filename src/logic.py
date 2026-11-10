import random

moves = ("rock", "paper", "scissors")
counter = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def computer_move():
    choice = random.choice(moves)
    return choice


print(computer_move)


def scores(player, computer_move):
    if player == computer_move:
        return "tie"
    elif counter[player] == computer_move:
        return "You win"
    else:
        return "Computer wins"


def game_data():
    return {"wins": 0, "losses": 0, "ties": 0}


# i know i need to print and keep returning ??
