'''n = int(input("Enter number: "))
inc = 1
fac = inc * n
for i in range (1,n+1):
    fac = inc * i
print(fac)'''

n = int(input("Enter number: "))
fact = 1

for i in range(1, n+1):
    fact = fact * i

print("The factorial of " + str(n) + " is : " + str(fact))