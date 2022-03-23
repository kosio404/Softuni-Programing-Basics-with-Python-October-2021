pages_per_book=int(input())
pages_per_hour=int(input())
day=int(input())
time_to_reed_the_book=pages_per_book/pages_per_hour
hours_needed=time_to_reed_the_book//day
print(hours_needed)