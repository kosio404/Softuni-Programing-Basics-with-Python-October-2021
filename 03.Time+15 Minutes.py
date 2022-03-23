current_hours=int(input())
current_minutes=int(input())
total_minutes=current_minutes+15
total_time=current_hours*60+total_minutes
hour=total_time//60
minutes=total_time%60
if hour>23:
    print(f'0:{minutes:02d}')
else:
    print(f'{hour}:{minutes:02d}')


