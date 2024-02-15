import random

number = random.randint(1, 100)
guess = None

print("Guess the number between 1 and 100: ")
def guess_game():
    guess = int(input())
    try:
        if guess < number:
            print("Too low! Take another Try: ")
            guess_game()
        elif guess > number:
            print("Too high! Take another Try: ")
            guess_game()
        else:
            print(f"Congratulations! You've guessed the number correctly")
    except ValueError:
        print("it's not a numeric value! Take another Try: ")
        guess_game()

guess_game()
