import random
secret_number = random.randint(1, 10)
guess = None
attempts = 0
while guess != secret_number:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
    except ValueError:
        print("Numbers only. Try again.")
print(f"You got it! It took you {attempts} attempts.")
