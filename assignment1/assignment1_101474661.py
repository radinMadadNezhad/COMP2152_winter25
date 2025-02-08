# Author: Radin Madad Nezhad Aligorkeh
# Assignment: #1

# Part b: Create 4 variables with comments for data types
gym_member = "Alex Alliton"  # str
preferred_weight_kg = 20.5   # float
highest_reps = 25            # int
membership_active = True     # bool

# Part c: Create a dictionary named workout_stats
# Dictionary with string keys and tuple values containing three integers
workout_stats = {
    "Alex": (30, 45, 20),   # (yoga, running, weightlifting)
    "Jamie": (40, 35, 25),
    "Taylor": (20, 50, 30)
}

# Part d: Calculate total workout minutes for each friend
# Iterate over a copy of the dictionary keys to avoid runtime errors
for friend in list(workout_stats.keys()):  # Use list() to create a copy of the keys
    total_minutes = sum(workout_stats[friend])
    workout_stats[f"{friend}_Total"] = total_minutes

# Part e: Create a 2-dimensional list called workout_list
# List of lists, where each inner list represents a friend's workout minutes
workout_list = [list(workout_stats[friend][:3]) for friend in workout_stats if "_Total" not in friend]

# Part f: Slice the workout_list
# Extract and print yoga and running minutes for all friends
print("Yoga and Running minutes for all friends:")
for friend in workout_list:
    print(friend[:2])

# Extract and print weightlifting minutes for the last two friends
print("\nWeightlifting minutes for the last two friends:")
for friend in workout_list[-2:]:
    print(friend[2])

# Part g: Check if any friend's total workout minutes are >= 120
for friend in workout_stats:
    if "_Total" in friend and workout_stats[friend] >= 120:
        print(f"\nGreat job staying active, {friend.split('_')[0]}!")

# Part h: Allow user to input a friend’s name and check if it exists
friend_name = input("\nEnter a friend's name: ")
if friend_name in workout_stats:
    print(f"\nWorkout minutes for {friend_name}:")
    print(f"Yoga: {workout_stats[friend_name][0]}")
    print(f"Running: {workout_stats[friend_name][1]}")
    print(f"Weightlifting: {workout_stats[friend_name][2]}")
    print(f"Total: {workout_stats[f'{friend_name}_Total']}")
else:
    print(f"\nFriend {friend_name} not found in the records.")

# Part i: Print the friend with the highest and lowest total workout minutes
# Create a dictionary of totals only for keys that end with "_Total"
totals = {friend: workout_stats[friend] for friend in workout_stats if friend.endswith("_Total")}

# Find the friend with the highest and lowest total workout minutes
max_friend = max(totals, key=totals.get)
min_friend = min(totals, key=totals.get)

print(f"\nFriend with the highest total workout minutes: {max_friend.split('_')[0]} ({totals[max_friend]} minutes)")
print(f"Friend with the lowest total workout minutes: {min_friend.split('_')[0]} ({totals[min_friend]} minutes)")