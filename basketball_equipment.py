price_for_year_training=int(input())
price_for_sneakers=price_for_year_training*0.6
price_for_clothes=price_for_sneakers*0.8
price_for_ball=price_for_clothes/4
accessories=price_for_ball/5
price_for_the_year=price_for_year_training+price_for_sneakers+price_for_clothes+price_for_ball+accessories
print(price_for_the_year)