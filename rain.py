a = int(input("Enter rain at 12 am: "))
b = int(input("Enter rain at 4 am: "))
c = int(input("Enter rain at 8 pm: "))
d = int(input("Enter rain at 12 pm: "))
e = int(input("Enter rain at 4 pm: "))
f = int(input("Enter rain at 8 pm: "))

avg = (a+b+c+d+e+f)/6

print("Avg rainfall today was " + str(avg) + "cm")

if (avg > 400):
    print("It rained severely")
elif (100 < avg < 400):
    print("It rained heavily")
elif (40 < avg < 100):
    print("It rained moderately")
else:
    print("It rained")
                     
rain = [a,b,c,d,e,f]

print("The most rainfall was " + str(max(rain)))  
