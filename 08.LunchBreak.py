from math import ceil
name=str(input())
lenght_of_episode=int(input())
lenght_of_lunch_break=int(input())
time_for_lunch=lenght_of_lunch_break/8
time_for_rest=lenght_of_lunch_break/4
lunch_and_rest_time=time_for_rest+time_for_lunch
time_left_for_episode=lenght_of_lunch_break-lunch_and_rest_time
diff=abs(time_left_for_episode-lenght_of_episode)
if time_left_for_episode>=lenght_of_episode:
    print(f"You have enough time to watch {name} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(diff)} more minutes.")
