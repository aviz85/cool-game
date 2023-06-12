import random

def cool_game():
    print("Welcome to the Cool Game!")
    print("I am thinking of a number between 1 and 100.")
    print("Try to guess it.")
    number = random.randint(1, 100)
    while True:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print("Congratulations! You guessed the number")
            break
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")

if __name__ == '__main__':
    cool_game()