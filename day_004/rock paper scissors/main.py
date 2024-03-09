import random
import os


def clear():
    """
    Function to clear the terminal on windows, mac and
    linux for a better user experience.
    """
    # for Windows
    if os.name == 'nt':
        os.system('cls')
    # for Mac and Linux (here, os.name is 'posix')
    else:
        os.system('clear')


def play_game():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    player_score = 0
    computer_score = 0

    # Write your code below this line 👇

    computer_choice = random.randint(0, 2)
    print("Welcome to Rock, Paper, Scissors game!")
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper\
or 2 for Scissors.\n"))

    if user_choice == 0:
        print(f"You chose: 0 \nrock {rock}")
        print(f"Computer chose: {computer_choice}")
        if computer_choice == 0:
            print(f"rock {rock}")
        elif computer_choice == 1:
            print(f"paper {paper}")
        elif computer_choice == 2:
            print(f"scissors {scissors}")
        else:
            print("Invalid input")
    elif user_choice == 1:
        print(f"You chose: 1 \npaper {paper}")
        print(f"Computer chose: {computer_choice}")
        if computer_choice == 0:
            print(f"rock {rock}")
        elif computer_choice == 1:
            print(f"paper {paper}")
        elif computer_choice == 2:
            print(f"scissors {scissors}")
        else:
            print("Invalid input")
    elif user_choice == 2:
        print(f"You chose: 2 \nscissors {scissors}")
        print(f"Computer chose: {computer_choice}")
        if computer_choice == 0:
            print(f"rock {rock}")
        elif computer_choice == 1:
            print(f"paper {paper}")
        elif computer_choice == 2:
            print(f"scissors {scissors}")
        else:
            print("Invalid input")
    else:
        print("Invalid input")

    if user_choice == 0 and computer_choice == 0:
        print("You chose rock and computer chose rock too. It's a draw!")
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose!")
        print("Paper wins against rock.")
        computer_score += 1
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
        print("Rock wins against scissors.")
        player_score += 1
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
        print("Paper wins against rock.")
        player_score += 1
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
    elif user_choice == 1 and computer_choice == 1:
        print("You chose paper and computer chose paper too. It's a draw!")
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose!")
        print("Scissors wins against paper.")
        computer_score += 1
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
        print("Rock wins against scissors.")
        computer_score += 1
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
        print("Scissors wins against paper.")
        player_score += 1
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
    elif user_choice == 2 and computer_choice == 2:
        print(
            "You chose scissors and computer chose scissors too. It's a draw!")
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")

    end_game = str(input("Play again? Enter Y or N: \n")).lower()
    if end_game == "y":
        clear()
        play_game()
        player_score = player_score
        computer_score = computer_score
    else:
        clear()
        print("Thanks for playing!")
        exit()


play_game()
