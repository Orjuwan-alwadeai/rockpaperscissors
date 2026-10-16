import random

options = ["rock", "paper", "scissors"]
computer = random.choice(options)

player = input("Enter rock, paper, or scissors: ").strip().lower()

if player not in options:
    print("Error: invalid input. Please enter rock, paper, or scissors.")
else:
    print(f"You played: {player}")
    print(f"Computer played: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")
