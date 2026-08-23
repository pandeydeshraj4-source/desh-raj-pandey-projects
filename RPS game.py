import random
choices = ("rock","paper","scissors")

print("Welcome to Rock, Paper and Scissors game")

user = input("Enter rock, paper, scissors: ").strip().lower()

computer = random.choice(choices)
print("Computer:",computer)

if user == computer:
    print("It's a draw")

elif user == "rock" and computer == "scissors":
    print("You win")
elif user == "paper" and computer == "rock":
    print("You win")
elif user == "scissors" and computer == "paper":
    print("You win")

else:
    print("Computer wins")

print("Thanks for playing!")