import random

def play_game():
    print("--- Welcome to Number Guessing Game (Advanced) ---")
    
    level = input("Choose difficulty (easy/hard): ").lower()
    max_num = 100 if level == "hard" else 20
    secret_number = random.randint(1, max_num)
    attempts = 5
    
    print(f"I'm thinking of a number between 1 and {max_num}. You have 5 chances!")

    while attempts > 0:
        try:
            guess = int(input(f"Enter your guess (Chances left: {attempts}): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess == secret_number:
            print(f"Boom! You guessed it in {6 - attempts} tries!")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
        
        attempts -= 1

    print(f"Game Over! The number was {secret_number}.")

play_game()