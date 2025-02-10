# Import the random library to use for dice rolling
import random

# Import all functions from functions_lab05
import functions_lab05

# Game Setup
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Weapons List
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Loot Options
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]
belt = []

# Monster Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Initialize Player and Monster Stats
num_stars = 0
input_invalid = True
attempts = 0

# Combat Strength Selection
while input_invalid and attempts < 5:
    print("    ------------------------------------------------------------------")
    combat_strength = input("Enter your combat Strength (1-6): ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input
    if not combat_strength.isnumeric() or not m_combat_strength.isnumeric():
        print("    |    Invalid input. Please enter integer values between 1 and 6.")
        attempts += 1
        continue

    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    if combat_strength not in range(1, 7) or m_combat_strength not in range(1, 7):
        print("    |    Please enter valid integers between 1 and 6 only.")
        attempts += 1
    else:
        input_invalid = False

if input_invalid:
    print("Too many invalid attempts. Exiting game.")
    exit()

# Roll for Weapon
input("Roll the dice for your weapon (Press enter)")
weapon_roll = random.choice(small_dice_options)
combat_strength = min(6, combat_strength + weapon_roll)

print(f"    |    The hero's weapon is {weapons[weapon_roll - 1]}")

# Weapon Strength Analysis
if weapon_roll <= 2:
    print("    |    --- You rolled a weak weapon.")
elif weapon_roll <= 4:
    print("    |    --- Your weapon is average.")
else:
    print("    |    --- Nice weapon!")

if weapons[weapon_roll - 1] != "Fist":
    print("    |    --- Thank goodness you didn't roll the Fist...")

# Roll for Player's Health Points
input("Roll the dice for your health points (Press enter)")
health_points = random.choice(big_dice_options)
print(f"    |    Player rolled {health_points} health points")

# Roll for Monster's Health Points
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(big_dice_options)
print(f"    |    Monster rolled {m_health_points} health points")

# Loot Collection
belt, loot_options = functions_lab05.collect_loot(belt, loot_options)

# Use Loot
print("!!You see a monster in the distance! You quickly use your first item:")
first_item = belt.pop(0)
if first_item in good_loot_options:
    health_points = min(6, health_points + 2)
    print(f"You used {first_item} to increase your health to {health_points}")
elif first_item in bad_loot_options:
    health_points = max(0, health_points - 2)
    print(f"You used {first_item} and lost health. New health: {health_points}")
else:
    print(f"You used {first_item}, but it's not helpful.")

# Compare Player vs. Monster Strength
print(f"    |    --- Strength Match: {combat_strength == m_combat_strength}")
print(f"    |    --- Strong Player: {combat_strength + health_points >= 15}")

# Roll for Monster's Power
input("Roll for Monster's Magic Power (Press enter)")
power_roll = random.choice(list(monster_powers.keys()))
m_combat_strength = min(6, m_combat_strength + monster_powers[power_roll])
print(f"    |    The monster's combat strength is now {m_combat_strength} using {power_roll} magic power")

# Battle Begins
print("You meet the monster. FIGHT!!")

# Roll to see who strikes first
attack_roll = random.choice(small_dice_options)
print(f"    |    Attack roll: {attack_roll}")

if attack_roll in [1, 3, 5]:  # Hero attacks first
    print("    |    Hero strikes first!")
    while m_health_points > 0 and health_points > 0:
        input("You strike first (Press Enter)")
        m_health_points = functions_lab05.hero_attacks(combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
            break
        input("The monster strikes (Press Enter)")
        health_points = functions_lab05.monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
            break
        num_stars = 2
else:  # Monster attacks first
    print("    |    Monster strikes first!")
    while m_health_points > 0 and health_points > 0:
        input("The monster strikes first (Press Enter)")
        health_points = functions_lab05.monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
            break
        input("You strike back (Press Enter)")
        m_health_points = functions_lab05.hero_attacks(combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
            break
        num_stars = 2

# Award Stars
stars = "*" * num_stars

# Get Hero's Name
while True:
    hero_name = input("Enter your Hero's name (two words): ")
    name_parts = hero_name.split()
    if len(name_parts) == 2 and all(part.isalpha() for part in name_parts):
        break
    print("Invalid input. Enter exactly two words with alphabetical characters only.")

# Shortened Hero Name
short_name = name_parts[0][:2] + name_parts[1][0]
print(f"Hero {short_name} gets <{stars}> stars")
print(f"Your hero's short name is: {short_name}")
