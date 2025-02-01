# Import the random library to use for the dice later
import random

# Hero's Attack Functions
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  
      """
    print(ascii_image)
    print("Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("You have killed the monster")
    else:
        m_health_points -= combat_strength
        print("You have reduced the monster's health to " + str(m_health_points))
    return m_health_points

# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("Monster's Claw (" + str(m_combat_strength) + ") ---> Hero (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 0
        print("You have killed the monster")
    else:
        health_points -= m_combat_strength
        print("The monster has reduced your health to " + str(health_points))
    return health_points

# Game Setup
# Define The number of lives for the Hero and Monster
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

# Define the Dice
diceOptions = list(range(1, 7))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]

# Define Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define empty belt
belt = []

# Define the number of stars awarded to the Player
num_stars = 0

# Print out the weapons using a for loop
print("Available Weapons:")
for weapon in weapons:
    print("- " + weapon)

# Use a While Loop to get valid input for Hero and Monster's Combat Strength
i = 0
while i in range(5):
    combat_strength = input("\nEnter your combat Strength (1-6): ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        print("One or more invalid inputs. Please enter integer numbers for Combat Strength")
        i = i + 1
        continue
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue
    else:
        break

# Input was valid - broke out of while loop
combat_strength = int(combat_strength)
m_combat_strength = int(m_combat_strength)

# Roll for weapon
input("\nRoll the dice for your weapon (Press Enter)")
weaponRoll = random.choice(diceOptions)
combat_strength = min(6, (combat_strength + weaponRoll))
print("The hero's weapon is " + str(weapons[weaponRoll - 1]))

# Weapon Roll Analysis
input("Analyze the Weapon roll (Press Enter)")
if weaponRoll <= 2:
    print("--- You rolled a weak weapon, friend")
elif weaponRoll <= 4:
    print("--- Your weapon is meh")
else:
    print("--- Nice weapon, friend!")

if weapons[weaponRoll - 1] != "Fist":
    print("--- Thank goodness you didn't roll the Fist...")

# Roll for Monster's Magic Power
input("\nRoll for monster's magic power (Press Enter)")
monster_power = random.choice(list(monster_powers.keys()))
power_strength = monster_powers[monster_power]
print(f"Monster rolled {monster_power} with strength {power_strength}")

# Update Monster's Combat Strength
m_combat_strength = min(6, m_combat_strength + power_strength)
print(f"Monster's updated combat strength: {m_combat_strength}")

# Roll for player health points
input("\nRoll the dice for your health points (Press Enter)")
health_points = random.choice(diceOptions)
print("Player rolled " + str(health_points) + " health points")

# Roll for monster health points
input("Roll the dice for the monster's health points (Press Enter)")
m_health_points = random.choice(diceOptions)
print("Player rolled " + str(m_health_points) + " health points for the monster")

# Analyze the roll
input("Analyze the roll (Press Enter)")
print("--- You are matched in strength: " + str(combat_strength == m_combat_strength))
print("--- You have a strong player: " + str((combat_strength + health_points) >= 15))

# Loot Collection System
print("\nYou found a loot bag!")
input("Roll for first loot item (Press Enter)")
first_loot = random.choice(loot_options)
loot_options.pop(loot_options.index(first_loot))
belt.append(first_loot)
print(f"Added {first_loot} to belt")
print(f"Current belt: {belt}")

input("\nRoll for second loot item (Press Enter)")
second_loot = random.choice(loot_options)
loot_options.pop(loot_options.index(second_loot))
belt.append(second_loot)
print(f"Added {second_loot} to belt")
print(f"Current belt: {belt}")

print("\nOrganizing your belt alphabetically...")
belt.sort()
print(f"Organized belt: {belt}")

# Use first loot item
print("\nYou see a monster in the distance! Time to use your first loot item.")
used_item = belt.pop(0)

if used_item in good_loot_options:
    health_points = min(6, health_points + 2)
    print(f"Used {used_item}. Health increased by 2!")
elif used_item in bad_loot_options:
    health_points = max(0, health_points - 2)
    print(f"Used {used_item}. Health decreased by 2!")
else:
    print(f"Used {used_item}. It wasn't particularly helpful.")

print(f"Your health is now {health_points}")
print(f"Remaining belt: {belt}")

# Main Combat Loop
print("\nYou meet the monster. FIGHT!!")
while m_health_points > 0 and health_points > 0:
    input("\nYou strike first (Press Enter)")
    m_health_points = hero_attacks(combat_strength, m_health_points)
    if m_health_points == 0:
        num_stars = 3
    else:
        input("\nThe monster strikes (Press Enter)")
        health_points = monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
        else:
            num_stars = 2

# Game End
stars = "*" * num_stars
print("\nHero gets <" + stars + "> stars")
print("\nGame Over!")