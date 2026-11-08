import random

print("Welcome to the Coin Guessing Game!")

print("Choose a method to toss the coin:")
print("1. Using random.random()")
print("2. Using random.randint()")

choice = input("Enter your choice (1 or 2): ")
random_choice = random.random()
random_choice_2 = random.randint(0,1)

if choice == "1":

    if random_choice >= 0.5:
        computer_result = "heads"
    else:
        computer_result = "tails"

elif choice == "2":
    if random_choice_2 == 0:
        computer_result = "heads"
    else:
        computer_result = "tails"

else:
    print("Invalid choice")

guess = input("Enter your Guess (Heads or Tails:) ").lower()

if guess == computer_result.lower():
    print("Congratulations! You won!")
else:
    print("Sorry, you lost!")

print(f"The computer coin yoss result was: {computer_result}")