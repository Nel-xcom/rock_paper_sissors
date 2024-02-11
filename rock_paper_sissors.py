"""
Quick game | Documentation

- Rock Paper Sissors | w/ Random Library and While loop

    . Some other knowledge applyed in this file are:
        - Style guide PEP-8 for a good syntax and documentation
        - Arithmetic operators
        - Logical operators
        - Conditionals if, else and elif.
        -Comparison operators
"""

#-- Libraries
import random



#-- User and computer score
user_score = 0
computer_score = 0



#-- Options [0, 1, 2]
options = ["rock", "paper", "sissors"]



#-- Game loop
while True:
    game_input = input("Choose rock, paper, sissors or 'q' to quit: ").lower()

    #--End the loop
    if game_input == "q":
        print("You won", user_score, "times")
        print("The computer won", computer_score, "times")
        break
    #-- user/list checker
    if game_input not in options:
        continue
    #-- Computer options
    random_option = random.randrange(0,2)
    # [rock: 0, paper: 1, scissors: 2]
    computer_pick = options[random_option]
    print("Computer picked", computer_pick, ".")

    #-- Game Scenarios
    if game_input == "rock" and computer_pick == "sissors":
        print("You win!")
        user_score += 1
    elif game_input == "sissors" and computer_pick == "paper":
        print("You win!")
        user_score += 1
    elif game_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_score += 1
    else:
        computer_score += 1
        print("I win 1 score! Let's see the next time...")


print("You won ", user_score, " times")
print("I won ", computer_score, " times")
print("Thanks for played!")
