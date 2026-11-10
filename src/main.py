print("Welcome to Rock Paper Scissors!")
name = input("What is your name? ")
print(f"Hello, {name.strip()}!")

from options import menu_options, player_choice, computer_move
from logic import scores


while player_choice() != "exit":

    def starting_app():
        print("Welcome to Rock Paper Scissors!")
        menu_options()
        player_choice()
        computer_move()
        print(scores(player_choice(), computer_move()))


if player_choice() == "exit":
    running = False

if __name__ == "__main__":
    starting_app()
