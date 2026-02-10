import random 

lowest_num = 1 
highest_num = 100
answer = random.randint(lowest_num, highest_num )
guesses = 0
is_running = True

print("Python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range ")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again dumbass!")
        else:
            print(f"CORRECT our answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False


    else:
        print("Enter a number asshole")
        print(f"Please select a number between {lowest_num} and {highest_num}")



