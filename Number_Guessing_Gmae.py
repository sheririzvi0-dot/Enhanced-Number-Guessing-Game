import random
print("========= Welcome to the Number Guessing Game! 😃🎮=========")
print("i will think of a number🤔, and you have to guess it.")

#Difficulty  selection
print("Difficulty Levels:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

levels=input("Select a difficulty level (1, 2, or 3): ")
if levels == "1":
    max_number = 50
    max_guesses = 10
    print("You have selected Easy level. You have 10 guesses to find the number between 1 and 50.")
elif levels == "2":
    max_number = 100
    max_guesses = 7
    print("You have selected Medium level. You have 7 guesses to find the number between 1 and 100.")
elif levels == "3":
    max_number = 200
    max_guesses = 5
    print("You have selected Hard level. You have 5 guesses to find the number between 1 and 200.")
else:
    print("Invalid Choice. Defaulting to Medium level.")
    max_number = 100
    max_guesses = 7

#Gerating a random number
random_number = random.randint(1, max_number)
attempts = 0

#Game loop
while attempts < max_guesses:
    guess = int(input(f"Guess a number between 1 and {max_number}: "))
    attempts += 1

    if guess < random_number:
        print("📉Too low! Try again.")
    elif guess > random_number:
        print("📈Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts! 🎉")
        break
    print(f"You have {max_guesses - attempts} guesses left.")
else:
    print(f"😢 You've used all your guesses. The number was {random_number}. Better luck next time!")