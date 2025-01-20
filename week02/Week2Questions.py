import random

# Step 1: Define the weapons array with increasing strength
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Step 2: Roll a dice (1-6) to select a weapon
try:
    weaponRoll = random.randint(1, 6)
    print(f"Dice rolled: {weaponRoll}")

    # Use the weaponRoll as an index to pick the weapon
    weapon = weapons[weaponRoll - 1]
    print(f"Hero's weapon: {weapon}")


    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    # Check if the weapon is not a Fist
    if weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")
except IndexError as e:
    print(f"Error: {e} - Weapon roll index is out of range.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
