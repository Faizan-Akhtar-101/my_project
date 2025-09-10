import random

random_num = random.randint(1, 100)
print("Welcome to Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print("Can you guess it? 🤔")
# Initialize attempts counter
attempts = 0
# Start guessing loop
while True:
    a = int(input("Enter your guess: "))
    attempts += 1  # Count each guess

    if a < random_num:
        print("Too Low! Try again.")
    elif a > random_num:
        print("Too High! Try again.")
    else:
        print(f"🎉 Congrats! You guessed the number {random_num} correctly in {attempts} attempts.")
        break

