city=str(input())
s=float(input())
if city=="Sofia" and 0<=s<=500:
    print(f"{s*0.05:.2f}")
elif city=="Sofia" and 500<s<=1000:
    print(f"{s*0.07:.2f}")
elif city=="Sofia" and 1000<s<=10000:
    print(f"{s*0.08:.2f}")
elif city=="Sofia" and s>10000:
    print(f"{s*0.12:.2f}")
elif city=="Varna" and 0<=s<=500:
    print(f"{s*0.045:.2f}")
elif city=="Varna" and 500<s<=1000:
    print(f"{s*0.075:.2f}")
elif city=="Varna" and 1000<s<=10000:
    print(f"{s*0.1:.2f}")
elif city=="Varna" and s>10000:
    print(f"{s*0.13:.2f}")
elif city=="Plovdiv" and 0<=s<=500:
    print(f"{s*0.055:.2f}")
elif city=="Plovdiv" and 500<s<=1000:
    print(f"{s*0.08:.2f}")
elif city=="Plovdiv" and 1000<s<=10000:
    print(f"{s*0.12:.2f}")
elif city=="Plovdiv" and s>10000:
    print(f"{s*0.145:.2f}")
else:
    print("error")