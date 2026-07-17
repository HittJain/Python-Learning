import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices = { "player" :player_choice, "computer":computer_choice }
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It is a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You WIN!"
        else:
            return "Paper covers rock! You LOSE."
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper! You LOSE."
        else:
            return "Paper covers rock! You WIN!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You WIN!"
        else:
            return "Rock smashes scissors! You LOSE."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)