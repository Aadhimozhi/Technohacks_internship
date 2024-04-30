import random

def determine_winner(player_choice, computer_choice):
    """Determines the winner of the game"""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Main function to play the game"""
    choices = ['rock', 'paper', 'scissors']
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_choice in choices:
            computer_choice = random.choice(choices)
            print(f"Computer chooses {computer_choice}")
            print(determine_winner(player_choice, computer_choice))
            break
        else:
            print("Invalid choice. Please enter either 'rock', 'paper', or 'scissors'.")

print("Welcome to Rock, Paper, Scissors!")
play_game()
