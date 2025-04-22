import random

def roll_dice():
    total = 0
    roll_history = []
    print("Your goal is to reach a minimum 50 to win the game")

    while total < 50:
        input("Press enter to roll the die")
        roll = random.randint(1,6)
        total += roll
        roll_history.append(roll)
        print(f"You rolled out a {roll}, You're total is now: {total}")

    print(f"You have reached a total of {total}, You win!")
    print(f"This is your roll history: {roll_history}")



roll_dice()



    
    
