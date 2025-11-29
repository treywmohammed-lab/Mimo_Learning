import random

print("Welcome! Let's play rock paper scissors. First to 5 wins!")
#Scoreboard to start the program
user_score: int = 0
computer_score: int = 0


while user_score < 5 and computer_score < 5: #Playing 5 rounds of Rock, Paper, or Scissors
    user_input = input("Please enter Rock, Paper, or Scissors: ")
    user_lower = user_input.lower()

    computer_choice = ["rock", "paper", "scissors"]
    computer_random = random.choice(computer_choice)

    print(user_lower)
    print(computer_random)

    if (user_lower == "rock" and computer_random == "scissors") or (user_lower == "paper" and computer_random == "rock") or (user_lower == "scissors" and computer_random == "paper"):
        winner = "User Wins"
        user_score += 1
        print(winner)
        print(f"User Score: {user_score}")
        print(f"Computer Score: {computer_score}")
                    
    elif (computer_random == "rock" and user_lower == "scissors") or (computer_random == "paper" and user_lower == "rock") or (computer_random == "scissors" and user_lower == "paper"):
        winner = "Computer Won"
        computer_score += 1
        print(winner)
        print(f"User Score: {user_score}")
        print(f"Computer Score: {computer_score}")
    else:
        print("Tie, Play again? ")
        print(f"User Score: {user_score}")
        print(f"Computer Score: {computer_score}")

    if computer_score == 5:
        print(f"I'm sorry the computer beat you.")
    elif user_score == 5:
        print("You won! Congratulations!")


