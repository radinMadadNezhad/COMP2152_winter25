# Import the random library to use for the dice later
import random

# Use Loot Function
def use_loot(belt, loot_options):
    print("!!You find a loot bag!! You look inside to find 2 items:")

    # First loot item
    input("Roll for first item (Press enter)")
    lootRoll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(lootRoll - 1)
    belt.append(loot)
    print("Your belt: ", belt)

    # Second loot item
    input("Roll for second item (Press enter)")
    lootRoll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(lootRoll - 1)
    belt.append(loot)
    print("Your belt: ", belt)

    # Organize belt alphabetically
    print("You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("Your belt: ", belt)

    return belt, loot_options


# Collect Loot Function (Modified)
def collect_loot(belt, loot_options):
    belt, loot_options = use_loot(belt, loot_options)
    return belt, loot_options


# Hero's Attack Function
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
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        m_health_points -= combat_strength
        print("    |    You have reduced the monster's health to: " + str(m_health_points))
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
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 0
        print("    |    Player is dead")
    else:
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

# Define the recursive inception_dream function
def inception_dream(crazy_level=0):
    # Base case: stop recursion and return 2
    if crazy_level == 3:
        return crazy_level + 2  # Add 2 to crazy_level at the base case
    else:
        crazy_level += 1  # Increment crazy_level
        print(f"Inception level {crazy_level}... Going deeper!")
        return inception_dream(crazy_level)  # Recursively call inception_dream()

# Main Game Logic
def game():
    # Initialize stats
    health_points = 10
    combat_strength = 5

    # Run the inception dream
    crazy_level = inception_dream()
    print(f"After the dream, crazy level is: {crazy_level}")

    # After the inception_dream finishes, reduce health and increase combat strength
    health_points -= 1
    combat_strength += crazy_level

    print(f"Health after dream: {health_points}")
    print(f"Combat strength after dream: {combat_strength}")

    # Additional game logic continues...

# Run the game
game()
