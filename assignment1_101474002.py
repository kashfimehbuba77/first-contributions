# (a)
# Author: Kashfi Mehbuba
#Assignment: #1

# (b)
gym_member = "Alex Alliton" #datatype: string
preferred_weight_kg = 20.5  #datatype: float
highest_reps = 25           #datatype: integer
membership_active = True    #datatype: boolean

# (c) Dictionary storing workout stats of 4 different friends with Tuples of 3 integers
workout_stats = {
    "Maliha": (30, 13, 20),   
    "Faiza": (25, 50, 29),  
    "Fariha": (55, 45, 25),
    "Tanima": (17, 26, 30)
}

print(workout_stats)

# (d)
for friend, minutes in list(workout_stats.items()):
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes

print(workout_stats)

# (e)
workout_list = [list(minutes) for minutes in workout_stats.values() 
                if isinstance(minutes, tuple)]

print(workout_list)


workout_list = [list(minutes) for minutes in workout_stats.values() if isinstance(minutes, tuple)]

# (f)
yoga_running = [row[:2] for row in workout_list]
print("Yoga & Running minutes for all friends:", yoga_running)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for last two friends:", weightlifting_last_two)


# (g)
for friend, total in workout_stats.items():
    if "_Total" in friend and total >= 120:
        original_name = friend.replace("_Total", "")
        print(f"Great job staying active, {original_name}!")

# (h)
friend_name = input("\nEnter a friend's name to check their workout stats: ")

if friend_name in workout_stats:
    yoga, running, weightlifting = workout_stats[friend_name]
    total_minutes = workout_stats.get(f"{friend_name}_Total", 0)
    print(f"\n{friend_name}'s Workout Stats:")
    print(f"Yoga: {yoga} minutes")
    print(f"Running: {running} minutes")
    print(f"Weightlifting: {weightlifting} minutes")
    print(f"Total Workout Minutes: {total_minutes}")
else:
    print(f"Friend {friend_name} not found in the records.")

# (i)
total_minutes_dict = {friend.replace("_Total", ""): total for friend, total in workout_stats.items() if "_Total" in friend}

highest_friend = max(total_minutes_dict, key=total_minutes_dict.get)
lowest_friend = min(total_minutes_dict, key=total_minutes_dict.get)

print(f"\nFriend with the highest total workout minutes: {highest_friend} ({total_minutes_dict[highest_friend]} minutes)")
print(f"Friend with the lowest total workout minutes: {lowest_friend} ({total_minutes_dict[lowest_friend]} minutes)")


