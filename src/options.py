import random

options = ["rock", "paper", "scissors"]
counter = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def menu_options():
    print("menu:")
    print("1. play round")
    print("2.View Stats")
    print("3. Exit\n")


def get_menu_choice():
    while True:
        choice = input("choose an action(enter1-4): ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("invalid choice please try again")


def player_choice():
    while True:
        move = input("Choose a move (rock, paper, or scissors): ").strip().lower()
        if move in options:
            return move
        print("Invalid move. Please type rock, paper, or scissors.")


def computer_move():
    choice = random.choice(options)

    if choice == counter[player_choice()]:
        print("computer chose", choice.capitalize())
    return choice
