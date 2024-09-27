N = int(input())
place = 0
product = 1
count = 0
rev = 0
if (N <= 999):
    print('Entered number is not a 4 or more than 4-digit number')
else:
    r = N % 10
    N = N // 10
    N1 = N
    N2 = N
    while(N2 > 0):
        N2 = N2 // 10
        count += 1
    place = 10 ** (count-2)
    while (N1 > 9):
        rmid = N1 % 10
        N1 = N1 // 10
        rev += rmid * place
        place = place / 10
        product *= rmid
rev = int(rev)
while (rev > 0):
    r2 = rev % 10
    rev //= 10
    print(r2,end=' ')
print()
print(product)