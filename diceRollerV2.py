import random


def diceRoller():
    rolls = input(f"\nHow many rolls?: ")
    dieType = input(f"How many sides?: ")
    number = int(rolls)
    sides = int(dieType)
    total = 0
    if rolls == '0':
        return
    else:
        print(f"Rolling {rolls}d{dieType}:")
        for x in range (1, number+1):
            roll = random.randint(1, sides)
            total = total + roll
            print(roll)
        print("Total", total)
        return diceRoller()

diceRoller()