import random

#Define the choices array
choices = ["Rock", "paper", "Scissors"]

def main():
    try:
        user_input = input("Please enter your choice (Rock, paper, scissors): ").capitalize()

        #Validate the user input
        if user_input not in choices:
            raise ValueError("Invalid choice!, Please enter Rock, Paper, Scissors")

        # Convert the user input to an index
        playerChoice = choices.index(user_input)

        computerChoice = random.randint(0, 2)

        print(f"Player choice:{choices[playerChoice]}")
        print(f"Computer choice choice:{choices[computerChoice]}")

        #Determine the winner
        if playerChoice == computerChoice:
            print("It's a tie!")
        elif (playerChoice == 0 and computerChoice == 2) or \
                (playerChoice == 1 and computerChoice == 0) or \
                (playerChoice == 2 and computerChoice == 1):
            print("player wins!")
        else:
            print("computer wins!")
    except ValueError as e:
        print(f"Error {e}")


# Run the game through the main function
if __name__ == '__main__':
    main()