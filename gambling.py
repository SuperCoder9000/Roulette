import random

def get_int_input(prompt, min_val=None, max_val=None):
    """Safely read an integer from user with optional bounds."""
    while True:
        s = input(prompt)
        try:
            v = int(s)
            if (min_val is not None and v < min_val) or (max_val is not None and v > max_val):
                print(f"Please enter a number between {min_val} and {max_val}.")
                continue
            return v
        except ValueError:
            print("Please enter a valid integer.")

def play_round(money):
    pool_min, pool_max = 1, 36   
    print(f"\nCurrent balance: {money}")
    bid = get_int_input("How much do you want to bet? ", min_val=1)
    if bid > money:
        print("You don't have enough balance for that bet.")
        return money, False 

    # choose bet type
    while True:
        bet_type = input("Bet options: even (E), odd (O), specific number (S). Choose E/O/S: ").strip().upper()
        if bet_type in ('E', 'O', 'S'):
            break
        print("Invalid option. Choose E, O, or S.")

    specific_number = None
    if bet_type == 'S':
        specific_number = get_int_input(f"Pick a number between {pool_min} and {pool_max}: ", pool_min, pool_max)

    result = random.randint(pool_min, pool_max)
    print(f"Roulette result: {result}")

    if bet_type == 'E':
        if result % 2 == 0:
            money += bid
            print(f"You won! You gain {bid}.")
        else:
            money -= bid
            print(f"You lost {bid}.")
    elif bet_type == 'O':
        if result % 2 == 1:
            money += bid
            print(f"You won! You gain {bid}.")
        else:
            money -= bid
            print(f"You lost {bid}.")
    else:  
        if result == specific_number:
            payout = bid * 35  
            money += payout
            print(f"Jackpot! Exact match. You win {payout}.")
        else:
            money -= bid
            print(f"No match. You lost {bid}.")

    return money, True

def main():
    money = 1000
    print("Welcome to simple roulette.")
    print("Starting balance:", money)

    while money > 0:
        cont = input("\nDo you want to continue? (Y/N): ").strip().upper()
        if cont == 'N':
            print("Thanks for playing. Final balance:", money)
            break
        elif cont != 'Y':
            print("Please answer Y or N.")
            continue

        money, ok = play_round(money)
        if not ok:
            print("Round couldn't be completed.")
            break

    if money <= 0:
        print("Game over, u broke ass giga_nigga")

if __name__ == "__main__":
    main()
