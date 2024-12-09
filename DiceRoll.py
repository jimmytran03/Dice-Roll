import random

def roll_dice():
    return random.randint(1, 6)

if __name__ == "__main__":
    while True:
        roll = input("Type 'roll' to roll the dice or 'exit' to quit: ")
        if roll == 'exit':
            break
        elif roll == 'roll':
            print(f"Rolled: {roll_dice()}")
        else:
            print("Invalid command.")
