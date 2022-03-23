budget=float(input())
number_of_statists=int(input())
clotes_price=float(input())
decore_price=budget*0.1
if number_of_statists>150:
    clotes_price=clotes_price*0.9
else:
    clotes_price=clotes_price
expences=decore_price+number_of_statists*clotes_price
difference=abs(expences-budget)
if expences>budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
