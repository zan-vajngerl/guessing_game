import random



def easy():
    SECRET = random.randint(1, 100)
    try_number = 1
    global easy_score

    print("You chose easy difficulty. Try and guess a number between 1 and 100")
    print("You have 20 tries")
    print("Good Luck!")
    print(SECRET) #testing purposes, immediately see number


    for x in range(20):
        guess = int(input(f"Try number {try_number}: "))
        try_number += 1
        if guess == SECRET:
            print ("Good job!")

            easy_score = try_number - 1
            break
        elif guess > SECRET:
            print("Nope! Too high.")
        else:
            print("Nope! Too low")


    print(f"The number we were looking for was {SECRET}")



def medium():
    SECRET = random.randint(1, 200)
    try_number = 1
    global medium_score

    print("You chose medium difficulty. Try and guess a number between 1 and 200")
    print("If you're less than 10 numbers from the secret number, you'll be HOT")
    print("If you're 10-20 numbers from the secret number, you'll be WARM")
    print("If you're 20 or more numbers from the secret number, you'll be COLD")
    print("You have 20 tries")
    print("Good Luck!")

    for x in range(20):
        guess = int(input(f"Try number {try_number}: "))
        try_number += 1
        if guess == SECRET:
            print("Good job!")
            score = try_number - 1
            medium_score = score

            break
        elif 10 > abs(guess - SECRET):
            print("Hot!")
        elif 20 > abs(guess - SECRET):
            print("Warm")
        else: print("Cold")

    print(f"The number we were looking for was {SECRET}")

def hard():
    SECRET = random.randint(1, 50)
    try_number = 1
    global hard_score

    print("You chose hard difficulty. Try and guess a number between 1 and 50")
    print("You have 20 tries")
    print("Good Luck!")

    for x in range(20):
        guess = int(input(f"Try number {try_number}: "))
        try_number += 1
        if guess == SECRET:
            print("Good job!")
            score = try_number - 1
            hard_score = score

            break
        else: print("Try again")

    print(f"The number we were looking for was {SECRET}")
