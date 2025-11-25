import random

def main():

    game_loop = True
    print("Rock, paper, or scissors? (r/p/s): ")
    choice = input().lower()
    while game_loop == True:
        if choice == "r" or choice == "p" or choice == "s": 
            cpu_choice = 
            print(f"You chose {choice}")
        else:
            print("Invalid choice")