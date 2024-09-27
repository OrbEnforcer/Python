n = int(input())
c = 0 
place = 0
n2 = n
num= 0
while(n>0):
    n = n // 10
    c += 1
place = 10 ** (c-1)
while (n2 > 0):
    r = n2 % 10
    n2 = n2 // 10
    num += r * place
    place //= 10
print(num)
