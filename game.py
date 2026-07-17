
import random


def roll_dice():
    return random.randint(1, 6)


def roll_dice_and_check_win():
    roll = random.randint(1, 6)

    if roll == 6:
        return "You win!"
    else:
        return "You lose!"
