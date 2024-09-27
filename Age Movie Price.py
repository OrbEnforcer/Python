age = float(input())
if age < 11.5 or age > 75:
    print("Not Eligible")
elif age >= 11.5 and age < 14.5:
    print(250)
elif age >= 14.5 and age < 25.5:
    print(275)
elif age >= 25.5 and age < 74.5:
    print(300)
