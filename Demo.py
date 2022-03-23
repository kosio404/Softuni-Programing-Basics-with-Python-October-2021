#round-закръгляне на някакво число, първо се въвежда числото, после запетая и число, което показва колко след десетичната запетая да се закръгли.
print(round(4.564476, 2))
print(round(4.566476, 2))
#форматиране- пак закръгляне, само че не изрязва нулите и цифрите, за разлика от горното, пази ги до посоченото число.
number=45.67852
print(f"{number:.8f}")
number1=45.0
print(f"{number:.2f}")
print(f"{number1:.3f}")


current_day="Monday"
if current_day=="Monday":
    salary=1000
    print(salary)

current_day= "Tuesday"
if current_day == "Monday":
     salary = 1000
     print(salary)