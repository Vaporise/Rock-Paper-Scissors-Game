import random

def main():

    game_loop = True
    
    

    while game_loop == True:
        
        choices = ["r", "p", "s"]

        print("Rock, paper, or scissors? (r/p/s): ")
        
        choice = input().lower()

        if choice == "r" or choice == "p" or choice == "s": 
            cpu_choice = random.choice(choices)
            print(f"You chose {choice}")
            print(f"The CPU chose {cpu_choice}")
            if choice == "r" and cpu_choice == "s":
                print("You win!")
            elif choice == "r" and cpu_choice == "r":
                print("It's a draw!")
            elif choice == "r" and cpu_choice == "p":
                print ("You lose")
            game_loop = False
        else:
            print("Invalid choice")
            game_loop = True

if __name__ == "__main__":
    main()