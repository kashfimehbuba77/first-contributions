# Author: Kashfi Mehbuba
#Assignment: #1

gym_member = "Alex Alliton" #datatype: string
preferred_weight_kg = 20.5  #datatype: float
highest_reps = 25           #datatype: integer
membership_active = True    #datatype: boolean

# Dictionary storing workout stats of 4 different friends with Tuples of 3 integers
workout_stats = {
    "Maliha": (30, 13, 20),   
    "Faiza": (25, 50, 29),  
    "Fariha": (55, 45, 25),
    "Tanima": (17, 26, 30)
}

print(workout_stats)

for friend, minutes in list(workout_stats.items()):
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes

print(workout_stats)


workout_list = [list(minutes) for minutes in workout_stats.values() 
                if isinstance(minutes, tuple)]

print(workout_list)


workout_list = [list(minutes) for minutes in workout_stats.values() if isinstance(minutes, tuple)]

yoga_running = [row[:2] for row in workout_list]
print("Yoga & Running minutes for all friends:", yoga_running)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for last two friends:", weightlifting_last_two)



