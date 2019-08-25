#!/usr/bin/env python3
#

import random
import time
from theseus_const import *


def initialize_theseus():
    """ Initialize variables """
    global weapons_theseus, safe_box
    # Intialize
    weapons_theseus = []
    safe_box = [*safe_box0]


def print_sleep0(message, wait_time=1):
    """ Default value to the wait_time parameter = 1
        so that if it is not specified when this function is called,
        then the default value will be used.
    """
    print(message)
    time.sleep(wait_time)


def print_sleep1(message):
    length = len(message)
    timing = int(length/(char_per_sec*2)) + wait_min
    print_sleep0(message, timing)


def print_sleepx(message):
    message = message.split("\n")
    for lines_in_message in message:
        print_sleep1(lines_in_message)


def valid_input(prompt, options):
    """
    e.g.
    choice = valid_input("Do you want to fight or run?\n", ['fight', 'run'])
    """
    while True:
        response = input(prompt)
        for option in options:
            if option in response.lower():
                return response.lower()
        print_pause(f'Sorry, I do not understand "{response}".')


def intro(hero, enemy):
    characters = {'hero': hero, 'enemy': enemy}
    theseus2 = theseus1.format(**characters)
    print_sleepx(theseus2)


def fight():
    # weapons_theseus contains the weapons - sword, 'ball',
    weapon = ""
    print_sleepx(f"The '{enemy}' attacks to eat you!")
    if 'sword' not in weapons_theseus:
        weapon = ""
    else:
        weapon = 'sword'
    choice = "x"
    while choice not in ['1', '2']:
        choice = input("Would you like to (1) fight or (2) run away? ")
        if choice == '1':
            if weapon == "":
                weapon = "strength"
                print_sleepx(f"You do your best...")
                print_sleepx(f"""\
but your only {weapon} is no match for the '{enemy}'.""")
                print_sleepx(f"""\
You will be eaten by the {enemy}!""")
            elif weapon == "sword":
                weapon2 = f"""\
As the '{enemy}' moves to eat you alive,
you unsheath The {ariadne_weapons['sword']} and kill the '{enemy}'!
You are victorious!
"""
                print_sleepx(weapon2)
        elif choice == '2':
            if 'sword' in weapons_theseus:
                print_sleepx("""\
You got the sword! You do not deserve the Princess!""")
            choice2 = """You run back into the labyrinth.
You are lost and the Minotaur will get you and eat you."""
            print_sleepx(choice2)


def labyrinth():
    if 'sword' in weapons_theseus:
        lab_str = f"""\
Next day, you approach the door of the labyrinth.
When you and the children from Athens enter the Labyrinth,
you tie the string to the door. Unroll it as you move through the maze.
That way, you can find your way back again.
This is the {enemy}'s house!"""
        print_sleepx(lab_str)
    else:
        weapon0 = f"""\
Next day, you approach the door of the labyrinth.
You and the children from Athens enter the Labyrinth.
Now, you feel bad without  Ariadne's sword."""
        print_sleepx(weapon0)


def challenge():
    print_sleepx(challenge1)       # 1 or 2
    choice = 'x'
    while choice not in ['1', '2']:
        choice = input("Please enter 1 or 2: ")

    if choice == '1':
        print_sleepx("""\
Love is in the air ...
You go into the room to find the safe box.""")
        while safe_box:
            weapon0 = room()      # Get sword, ball
            if len(safe_box) > 0:
                print_sleepx(f"""\
- You only got the '{weapon0}', says the Princess.""")
                print_sleepx("""\
- Go back and get all the stuff you need, say Ariadne to you.""")
                print_sleepx("""\
You go back into the room again to get all the missing stuff.""")
        print_sleepx("""\
- Now you got all the stuff you need! Congratulations! Say Ariadne.""")
        print_sleepx("""\
- Next step: go to the labyrinth, kill the Minotaur and marry me!""")
    elif choice == '2':
        no_deal = """
No deal! No Love!
Next day Theseus (you) will goe into the labyrinth cave without the sword
and no clue to get out if you kill the Minotaur."""
        print_sleepx(no_deal)
    #
    print_sleepx("")
    print_sleepx("\t*** Are you ready to fight and kill the Minotaur? ***")
    print_sleepx("")


def play_againx():
    print_sleepx("-" * line_len)
    print_sleepx("")
    choice = '--no-choice---'
    while choice not in ['y', 'Y', 'n', 'N', '']:
        choice = input("Would you like to play again? (y=Enter/n)[y] ")
        choice = choice.upper()
        if choice == 'N':
            print_sleepx("""\
Ariadne wants thank you for playing! Bye!""")
            return 'no_play_again'
        elif choice == 'Y' or choice == '':
            print_sleepx("Ariadne loves you!")
            return 'play_again'


def room():
    if not safe_box:      # ball and sword got
        print_sleepx(safe0)
        print_sleepx(f"You walk back out to princess Ariadne.")
    else:
        # Requirement from project: to use random.randint or random.choice
        # weapon0 = sr.choice(safe_box)
        #
        weapon0 = random.choice(safe_box)
        weapons_theseus.insert(0, weapon0)
        safe_box.remove(weapon0)
        weapont = {'weapon': weapon0}
        safe1 = safe_box_mes[weapon0]
        safe1b = safe1.format(**weapont)
        print_sleepx(safe1b)
        back2ariadne = f"""\
You walk back out to princess Ariadne with the `{weapon0}`."""
        print_sleepx(back2ariadne)
    return weapon0


if __name__ == '__main__':
    game_state = 'play_again'
    while game_state == 'play_again':
        initialize_theseus()
        print_sleepx("-" * line_len)
        numb0 = time.time()
        numb = int(numb0)
        #
        # random.seed(numb0)	    # or random.seed(numb) - an integer.
        # sr = random.SystemRandom()
        # enemy = sr.choice(enemies)
        # Requirement from project: to use random.randint or random.choice
        #
        enemy = random.choice(enemies)
        #
        intro(hero, enemy)
        challenge()
        labyrinth()
        fight()
        game_state = play_againx()
else:
    print("Importing...")
