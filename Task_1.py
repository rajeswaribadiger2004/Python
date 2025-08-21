import random

def guessing_game():
    # Randomly choose a number between 1 and 100
    secret_number = random.randint(1, 100)
    //hello
    attempts = 0
    guessed = False
    
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Your goal is to guess the correct number.")
    print("After each guess, I'll tell you if your guess is too high, too low, or correct.")
    print("Let's begin!\n")

    while not guessed:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Conditional logic to guide the player
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"\nCongratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()

#OUTPUT
'''
Welcome to the Guessing Game!
I have chosen a number between 1 and 100.
Your goal is to guess the correct number.
After each guess, I'll tell you if your guess is too high, too low, or correct.
Let's begin!

Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 30
Too low! Try again.
Enter your guess: 40
Too low! Try again.
Enter your guess: 45
Too low! Try again.
Enter your guess: 47
Too high! Try again.
Enter your guess: 46

Congratulations! You guessed the number 46 correctly in 7 attempts.'''