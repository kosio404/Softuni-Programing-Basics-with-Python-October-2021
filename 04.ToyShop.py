price_puzzle=2.6
price_talking_toy=3
pricce_teddy_bear=4.1
price_minion=8.2
price_truck=2
price_excursion=float(input())
number_puzzle=int(input())
number_talking_toy=int(input())
number_teddy_bear=int(input())
number_minion=int(input())
number_truck=int(input())
sum_number=number_puzzle+number_talking_toy+number_teddy_bear+number_minion+number_truck
total_price_toys=price_puzzle*number_puzzle+price_talking_toy*number_talking_toy+pricce_teddy_bear*number_teddy_bear+\
                 price_minion*number_minion+price_truck*number_truck
if sum_number>=50:
    total_price_toys=total_price_toys*0.75
else:
    total_price_toys=total_price_toys
money_left=total_price_toys*0.9
if money_left>=price_excursion:
    print(f"Yes! {(money_left-price_excursion):.2f} lv left.")
else:
    print(f'Not enough money! {(price_excursion-money_left):.2f} lv needed.')
