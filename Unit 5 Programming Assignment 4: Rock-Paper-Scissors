"""
Author: Marko 
Date: 2024-12-11
Description: This script plays a game of rock-paper-scissors
             with yourself and a computer.
"""

import random

def play_game():
    # Display options for the user
    print("Welcome to Rock-Paper-Scissors!")
    print("You can choose: r for Rock, p for Paper, s for Scissors")

    # Ask how many games the user wants to play
    num_games = int(input("How many games do you want to play? "))

    # Initialize scores
    player_wins = 0
    computer_wins = 0
    ties = 0

    # Loop for the number of games
    for game in range(num_games):
        # Get player's choice
        player_choice = input("Enter your choice (r, p, or s): ").lower()

        # Ensure the player enters a valid choice
        while player_choice not in ['r', 'p', 's']:
            player_choice = input("Invalid choice. Please enter 'r' for Rock, 'p' for Paper, or 's' for Scissors: ").lower()

        # Computer makes a random choice using random.randint(1, 3)
        computer_choice_num = random.randint(1, 3)
        if computer_choice_num == 1:
            computer_choice = 'r'  # Rock
        elif computer_choice_num == 2:
            computer_choice = 'p'  # Paper
        else:
            computer_choice = 's'  # Scissors

        # Print choices
        print(f"Your choice: {player_choice}")
        print(f"Computer's choice: {computer_choice}")

        # Determine the outcome of the game
        if player_choice == computer_choice:
            print("It's a tie!")
            ties += 1
        elif (player_choice == 'r' and computer_choice == 's') or \
             (player_choice == 'p' and computer_choice == 'r') or \
             (player_choice == 's' and computer_choice == 'p'):
            print("You win this round!")
            player_wins += 1
        else:
            print("Computer wins this round!")
            computer_wins += 1

    # Output the final scores
    print("\nGame Over!")
    print(f"Total player wins: {player_wins}")
    print(f"Total computer wins: {computer_wins}")
    print(f"Total ties: {ties}")

# Run the game
if __name__ == "__main__":
    play_game()
