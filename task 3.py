import random

def get_user_choice():
    choice = input("Choose [rock], [paper], or [scissors]: ").strip().lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Choose [rock], [paper], or [scissors]: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock-Paper-Scissors!")
    
    while True:
        print(f"\n🔄 Round {round_number}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n🧑 You chose: {user_choice}")
        print(f"🤖 Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("🔁 It's a tie!")
        elif result == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round.")
            computer_score += 1

        print(f"\n📊 Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        while play_again not in ["yes", "no", "y", "n"]:
            play_again = input("Please type 'yes' or 'no': ").strip().lower()

        if play_again in ["no", "n"]:
            print("\n👋 Thanks for playing! Final Score:")
            print(f"🏁 You: {user_score} | Computer: {computer_score}")
            break

        round_number += 1

# Run the game
if __name__ == "__main__":
    play_game()
