deposit=float(input())
deposit_term=int(input())
interest_rate=float(input())/100
accured_interest=deposit*interest_rate
accured_interest_per_month=accured_interest/12
amount=deposit+deposit_term*((deposit*interest_rate)/12)
print(amount)