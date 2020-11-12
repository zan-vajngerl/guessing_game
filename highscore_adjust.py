import json



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

def highscore_change(my_score):
    from main import difficulty
    first_place = get_scores(difficulty).first
    second_place = get_scores(difficulty).second
    third_place = get_scores(difficulty).third
    print(first_place)
    print(second_place)
    print(third_place)
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