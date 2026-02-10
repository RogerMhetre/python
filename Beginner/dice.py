import random 

dice_art = {
    1: ("┌─────────┐",       
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",       
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",       
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",       
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",       
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",       
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}   

while True:
    choice = input("Press Enter to roll dice or type 'q' to quit: ").lower()
    if choice == "q":
        break

    dice = []
    total = 0
    num_dice = int(input("Enter the number of dice: "))

    for _ in range(num_dice):
        dice.append(random.randint(1, 6))

    for line in range(5):
        for die in dice:
            print(dice_art[die][line], end=" ")
        print()

    total = sum(dice)
    print(f"Total: {total}\n")
