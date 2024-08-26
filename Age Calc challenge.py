import random
import time


def typewrite(num1, num2, text):
    for c in text:
        r = random.uniform(num1, num2)
        time.sleep(r)
        print(c, end='', flush=True)

msg = "The date format is m-yyyy"

for a in msg:
    typewrite(0.05, 0.25,a )


month = input("\nMonth: ")
 

for b in month:
    typewrite(0.05,0.25,b)


year = input("\nYear: ")


for c in year:
    typewrite(0.05,0.25,c)


age = 2023 - int(year)


age_calc = "\nYou were born "+ str(age) +" years ago!"

for d in age_calc:
    typewrite(0.05,0.25,d)
