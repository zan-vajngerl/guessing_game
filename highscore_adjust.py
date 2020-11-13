import json


# get_scores pulls the highscore information from the appropriate txt file depending on the difficulty
# as far as I know, this works
def get_scores(diff):
    global first
    global second
    global third
    if diff == "easy":

        with open("high_scores_easy.txt") as top_scores:
            scores = json.load(top_scores)

            first_place = scores["first"]["guesses"]
            second_place = scores["second"]["guesses"]
            third_place = scores["third"]["guesses"]
            first = first_place
            second = second_place
            third = third_place

    elif diff == "medium":
        with open("high_scores_medium.txt") as top_scores:
            scores = json.load(top_scores)

            first_place = scores["first"]["guesses"]
            second_place = scores["second"]["guesses"]
            third_place = scores["third"]["guesses"]
            first = first_place
            second = second_place
            third = third_place

    elif diff == "hard":
        with open("high_scores_hard.txt") as top_scores:
            scores = json.load(top_scores)

            first_place = scores["first"]["guesses"]
            second_place = scores["second"]["guesses"]
            third_place = scores["third"]["guesses"]
            first = first_place
            second = second_place
            third = third_place

# the purpose of highscore_change was to check whether the score from the user was in the top 3, then update the values
# if this is run, the guessing game loops on the same difficulty. If commented out the game function exits normally
# currently does not work, not sure why. My guess is I'm referencing the original scores incorrectly
def highscore_change(my_score):
    from main import difficulty
    first_place = get_scores(difficulty).first
    second_place = get_scores(difficulty).second
    third_place = get_scores(difficulty).third
    
    if my_score < third_place:
        if my_score < first_place:
            third_place = second_place
            second_place = first_place
            first_place = my_score
        elif first_place <= my_score < second_place:
            third_place = second_place
            second_place = my_score
        else:
            third_place = my_score

#still missing: updating the highscore files with the new results