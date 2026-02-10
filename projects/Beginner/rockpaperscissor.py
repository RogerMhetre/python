import random 

options = ("rock", "paper" , "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors): ").lower().strip()
        if player not in options:
            print(f"You can't pick a {player}")

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a Tie")
    elif player == "rock" and computer == "scissors":
        print("Player Wins")
    elif player == "paper" and computer == "rock":
        print("Player Wins")
    elif player == "scissors" and computer == "paper":
        print("Player Wins")
    else:
        print("Computer Wins")

    if not input("Play again? (y/n) : ").lower() == "y" :
        running = False

print("Thanks for playing!")