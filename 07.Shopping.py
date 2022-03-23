budget=float(input())
number_of_videocards=int(input())
number_of_processors=int(input())
number_of_RAM=int(input())
vidneocard_price=250
processor_price=vidneocard_price*number_of_videocards*0.35
RAM_price=vidneocard_price*number_of_videocards*0.1
total_price=vidneocard_price*number_of_videocards+processor_price*number_of_processors+number_of_RAM*RAM_price
if number_of_videocards>number_of_processors:
    total_price=total_price*0.85
diff=abs(total_price-budget)
if budget>=total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
