# Theseus game

line_len = 79
char_per_sec = 100           # 25 is normal
wait_min = 1                 # 1: should be ok, 0: fast, least 1 seg per line
game_state = 'running'
# ####
ariadne_weapons0 = {'sword': 'Sword of Ariadne', 'ball': 'Ball of string'}
ariadne_weapons = ariadne_weapons0
hero = "Theseus"
enemies = ['Minotaur']
# , 'troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
weapons_theseus = []
# This is an empty list ^
safe_box0 = ['ball of string', 'sword']		# This is a list
safe_box = [*safe_box0]
safe0 = """You already got the sword and the ball."""
# safe_sword = """It turns out to be a big safe box.
safe_sword = """You have found the magical {weapon}!"""
# Your eye catches a glint of metal behind a drawer.
# Sword of Ariadne , ball
safe_ball = """This time you get the ball so you can get out of the
Minotaur maze."""
safe_box_mes = {'sword': safe_sword, 'ball of string': safe_ball}
# safe_box_mes = {safe_box['sword']: safe_sword, safe_box['ball']: safe_ball}
# Intro
theseus1 = r"""You are Prince {hero} of Athens.
And bravely told your father (the king of Athens) that you are going to
Crete as the seventh son of Athens to kill the {enemy} and end the terror.
Theseus (you) took the place as the seventh Athenian boy.
Along with six other Athenian boys and seven Athenian girls,
Prince Theseus sailed towards Crete.
When the prince and the children arrived, King Minos and his daughter,
Princess Ariadne, came out to greet them.
The king told them that they would not be eaten until the next day and to
feel free to enjoy themselves in the palace in the meantime.
Late that night, the Princess Ariadne wrote Prince Theseus
a note and slipped it under his bedroom door.

---
Dear Theseus,
Without my help, the Minotaur will surely gobble you up.
I know a trick or two that will save your life.
If I help you kill the monster, you must promise to take me away from
this tiny island and marry me. If interested in this deal, meet me by
the gate to the Labyrinth in one hour.

Yours very truly,
Princess Ariadne
---

Prince Theseus slipped out of the palace and waited Princess Ariadne.
Ariadne pointed out a safe box in a room where it contains
the 'sword' to kill the Minotaur and the 'ball of string'
to get out the labyrinth.
Theseus should promise to take her away from the tiny island and marry her.
"""
# Minotaur or  {enemies[0]}  # 0=hero(Theseus), 1=Minotaur
challenge1 = """Enter 1 to accept the deal and enter the room to get
the 'sword' and the 'ball of string'.
Enter 2 to not accept the deal and fight against the Minotaur
with your own strength.
What would you like to do?"""
