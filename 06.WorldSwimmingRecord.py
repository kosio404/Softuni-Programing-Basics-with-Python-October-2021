world_record=float(input())
distance=float(input())
time_in_sec=float(input())
ivan_time=distance*time_in_sec
additional_time=int(distance/15)*12.5
total_time=ivan_time+additional_time
difference=abs(total_time-world_record)
if total_time<world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")