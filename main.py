import random

def main():

    game_loop = True #Set the state of the game loop
    
    wins = 0 #Wins counter
    draws = 0 #Draws counter
    losses = 0 #Loses counter

    choices = ["r", "p", "s"] #List of the choices.
    rules = { # a dictionary of the win conditions.
        "r": "s", #rock beats scissors
        "p": "r", #paper beats rock
        "s": "p" #scissors beats paper
    }

    while game_loop == True: # Game loop starts
        
        

        print("Rock, paper, or scissors? (r/p/s): ")
        
        choice = input().lower() #Take input and convert it to lower case.

        if choice in choices: #redid this code to make it easier to read and more concise. Before I had the options listens now it just works with my choices list.
            cpu_choice = random.choice(choices)
            print(f"You chose {choice}")
            print(f"The CPU chose {cpu_choice}")

            if choice == cpu_choice: #if the choices match its a draw.
                print("It's a draw!")
                draws += 1
            elif rules[choice] == cpu_choice: #if the value matches the cpu choice then the player make a winning choice. e.g rules[r] = s and opponent choice s.
                print("You win!")
                wins += 1
            else:
                print("You lose!") #
                loses += 1

            print(f"Wins:{win}, Draws: {draws}, Losses: {losses}") #Print the current score out.

            #Play again code
            play_again = input("Play again? (y/n)").lower()
            if play_again == "n":
                game_loop = False


        else:
            print("Invalid choice")

if __name__ == "__main__":
    main() 