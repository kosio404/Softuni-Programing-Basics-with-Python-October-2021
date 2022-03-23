fruit=str(input())
day=str(input())
quantity=float(input())
price=0
if fruit=="banana" and day=="Monday" or fruit=="banana" and day=="Tuesday" or fruit=="banana" and day=="Wednesday" \
        or fruit=="banana" and day=="Thursday" or fruit=="banana" and day=="Friday":
    price=2.50
    print(f"{price * quantity:.2f}")
elif fruit=="apple" and day=="Monday" or fruit=="apple" and day=="Tuesday" or fruit=="apple" and day=="Wednesday" \
        or fruit=="apple" and day=="Thursday" or fruit=="apple" and day=="Friday":
    price=1.20
    print(f"{price * quantity:.2f}")
elif fruit == "orange" and day == "Monday" or fruit == "orange" and day == "Tuesday" or fruit == "orange" and day == "Wednesday" \
        or fruit == "orange" and day == "Thursday" or fruit == "orange" and day == "Friday":
    price = 0.85
    print(f"{price * quantity:.2f}")
elif fruit == "grapefruit" and day == "Monday" or fruit == "grapefruit" and day =="Tuesday" or fruit == "grapefruit" and day =="Wednesday"\
        or fruit == "grapefruit" and day =="Thursday" or fruit == "grapefruit" and day =="Friday":
    price = 1.45
    print(f"{price * quantity:.2f}")
elif fruit == "kiwi" and day == "Monday" or fruit == "kiwi" and day == "Tuesday" or fruit == "kiwi" and day == "Wednesday" \
        or fruit == "kiwi" and day == "Thursday" or fruit == "kiwi" and day == "Friday":
    price = 2.70
    print(f"{price * quantity:.2f}")
elif fruit=="pineapple" and day == "Monday" or fruit=="pineapple" and day == "Tuesday" or fruit=="pineapple" and day == "Wednesday" \
        or fruit=="pineapple" and day == "Thursday" or fruit=="pineapple" and day == "Friday":
    price = 5.5
    print(f"{price * quantity:.2f}")
elif fruit=="grapes" and day == "Monday" or fruit=="grapes" and day == "Tuesday" or fruit=="grapes" and day == "Wednesday" \
        or fruit=="grapes" and day == "Thursday" or fruit=="grapes" and day == "Friday":
    price = 3.85
    print(f"{price * quantity:.2f}")
elif fruit=="banana" and day=="Saturday" or fruit=="banana" and day=="Sunday":
    price=2.70
    print(f"{price * quantity:.2f}")
elif fruit=="apple" and day=="Saturday" or fruit=="apple" and day=="Sunday":
    price=1.25
    print(f"{price * quantity:.2f}")
elif fruit == "orange" and day=="Saturday" or fruit == "orange" and day=="Sunday":
    price = 0.9
    print(f"{price * quantity:.2f}")
elif fruit == "grapefruit" and day=="Saturday" or fruit == "grapefruit" and day=="Sunday":
    price = 1.6
    print(f"{price * quantity:.2f}")
elif fruit == "kiwi" and day=="Saturday" or fruit == "kiwi" and day=="Sunday":
    price = 3
    print(f"{price * quantity:.2f}")
elif fruit=="pineapple" and day=="Saturday" or fruit=="pineapple" and day=="Sunday":
    price = 5.6
    print(f"{price * quantity:.2f}")
elif fruit=="grapes" and day=="Saturday" or fruit=="grapes" and day=="Sunday":
    price = 4.2
    print(f"{price * quantity:.2f}")
else:
    print("error")



