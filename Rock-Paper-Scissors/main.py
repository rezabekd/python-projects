from art import rock, paper, scissors
import random

computer_moves_list = [rock, paper, scissors]
computer_move_select = random.choice(computer_moves_list)

game_on = True

print("Welcome to the rock, paper, scissor best of 5 match!")

user_points = 0
computer_points = 0


def player_moves_print():
    if user_move == "r":
        print(f"{rock}\n You have played rock.")
    elif user_move == "p":
        print(f"{paper}\n You have played paper.")
    elif user_move == "s":
        print(f"{scissors}\n You have played scissors.")


def computer_moves_print():
    if computer_move == rock:
        print(f"{rock}\n Computer have played rock.")
    elif computer_move == paper:
        print(f"{paper}\n Computer have played paper.")
    elif computer_move == scissors:
        print(f"{scissors}\n Computer have played scissors.")


while game_on:
    user_move = input(f"Insert 'r' for rock, 'p' for paper or 's' for scissors. ").lower()
    computer_move = computer_move_select

    player_moves_print()
    computer_moves_print()

    if user_move == "r" and computer_move == scissors or user_move == "p" and computer_move == rock \
            or user_move == "s" and computer_move == paper:
        user_points += 1
        print(f"You win this round, your score is {user_points}, computer have {computer_points}.")

    elif user_move == "r" and computer_move == paper or user_move == "p" and computer_move == scissors \
            or user_move == "s" and computer_move == rock:
        computer_points += 1
        print(f"You lose this round, your score is {user_points}, computer have {computer_points}.")

    else:
        print(f"Draw! Your score is {user_points}, computer have {computer_points}.")

    if user_points == 3:
        game_on = False
        print("You have won the game!")
    elif computer_points == 3:
        game_on = False
        print("You have lost the game!")


