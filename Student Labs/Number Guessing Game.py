import random

def generate_random_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)

def get_user_guess():
    """Prompts the user to enter a guess and returns it."""
    guess = int(input("Enter your guess (between 1 and 100): "))
    return guess

def check_guess(secret_number, user_guess):
    """Compares the user's guess with the secret number and provides feedback."""
    if user_guess == secret_number:
        print("Congratulations! You guessed the correct number!")
    elif user_guess < secret_number:
        print("Too low. Try guessing a higher number.")
    else:
        print("Too high. Try guessing a lower number.")

def play_game():
    """Plays the number guessing game."""
    secret_number = generate_random_number()
    attempts = 0
    while True:
        attempts += 1
        guess = get_user_guess()
        check_guess(secret_number, guess)
        if guess == secret_number:
            break
    print(f"You made {attempts} attempts to guess the number.")

# Start the game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
play_game()


