# Taking input    
n = int(input("Enter number: "))
m = int(input("Enter mumber: "))
c = 0
for i in range (1,n):
    if (n % i == 0):
        c = c + 1
if (c == 1):
    print("The number is prime.")
else:
    print('The number is composite')
# In range
#for i in range(m,n):
#    for j in range(m,n):
#        if i%j == 0:
#            break
#    if i == j:
#        print(i,end=",")
