hour=int(input())
day=str(input())
if 10<=hour<=18 and day!="Sunday":
    print("open")
else:
    print("closed")