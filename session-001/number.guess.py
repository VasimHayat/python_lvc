import random

def guess_number():
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while guess != number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You got it! The number was", number)
            print("It took you", attempts, "attempts.")

guess_number()
