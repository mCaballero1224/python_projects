import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.\n").lower()

    if user_input == "q":
        print("User wins:", user_wins)
        print("Computer wins:", computer_wins)
        print("Good game!")
        quit()

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("Tie!")
        continue

    if (user_input == "rock" and computer_pick == "scissors") or (user_input == "paper" and computer_pick == "rock") or (user_input == "rock" and computer_pick == "scissors"):
        print("You won!")
        user_wins += 1
        continue
    else:
        print("You lost!")
        computer_wins += 1
        continue


