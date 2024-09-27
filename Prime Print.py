n1 = int(input())
n2 = int(input())
c = 0
for i in range (n1,n2):
    for j in range (n1,n2):
        if (i % j == 0):
            c += 1            
    if (c > 1):
        print('\n')
    else:
        print(i)
