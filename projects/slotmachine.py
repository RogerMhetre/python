#!/usr/bin/env python3
import random
import time


def spin_row():
    symbols = ['🍒', '🍑', '🍋', '👅', '🗿']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row [0] == '🍒':
            return bet * 3
        elif row[0] == '🍑':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '👅':
            return bet * 10  
        elif row[0] == '🗿':
            return bet * 20
    return 0

def main():
    balance = 100
    print("***********************")
    print("Welcome to ")
    print("Symbols: 🍒 🍑 🍋 👅 🗿")
    print("***********************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your Bet amount(q for quit): ").lower()

        if bet == 'q':
            break

        if not bet.isdigit():
            print(f"{bet} is not a valid number ")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficent funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0 ")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        elif balance == 0:
            print("Hey Nigga You are Bankrupt")

        balance += payout
    
    print("---------------------------------------")
    print(f"Game Over! Final Balance: ${balance}")
    print("---------------------------------------")


if __name__ == '__main__':
    main()
