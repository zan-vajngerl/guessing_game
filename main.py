from highscore_adjust import *
from games import *

print("Welcome to the guessing game")
name = input("What is your name? ")


while True:
    select_dif = input("Please select your difficulty (Easy/Medium?Hard): ").casefold()
    global difficulty
    difficulty = select_dif

    if difficulty == "easy":
        get_scores(difficulty)
        easy()
        highscore_change(easy().easy_score)
        #print(highscore_change().first_place)
        break
    elif difficulty == "medium":
        get_scores(difficulty)
        medium()
        highscore_change(medium().medium_score)
        break
    elif difficulty == "hard":
        get_scores(difficulty)
        hard()
        highscore_change(hard().hard_score)
        break
    else:
        print("Not a valid difficulty, please enter one of the given options")

input("Press enter to play again")