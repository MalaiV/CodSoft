import random
def get_player():
    player_choice = int(input("""WELCOME TO GAME
    0)Rock
    1)Scissors
    2)Paper          
    Select your choice : """))
    if 0 <= player_choice <= 2:
        return player_choice
    else:
        print("Invalid choice! Please select 0, 1, or 2.")
        return get_player()  # Recursive call

def get_Computer():
    return random.randint(0, 2)

def determine_winner(player, Computer):
    if player == Computer:
        return "Tie!! "
    elif (player - Computer) % 3 == 1:
        return "Computer"
    else:
        return "Player"

def display_result(player, Computer, winner):
    choices = ["Rock", "Scissors","Paper" ]
    print(f"You chose {choices[player]}")
    print(f"Computer chose {choices[Computer]}")
    print(f"Winner: {winner}")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        player = get_player()
        Computer = get_Computer()
        winner = determine_winner(player, Computer)
        display_result(player, Computer, winner)

        if winner == "Player":
            user_score += 1
        elif winner == "Computer":
            computer_score += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer")
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()

        if play_again == "no":
            break

    print("\nThanks for playing!")

if __name__ == "__main__":
    play_game()
