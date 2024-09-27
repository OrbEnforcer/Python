l1,le,lo = [],[],[]
c,s = 0,0
for i in range (10):
    l1.append(input())
z = l1[0]
y = z.split('=')
l1[0] = y[len(y)-1]
for j in range(len(l1)):
    if(int(l1[j]) % 2 == 0):
        le.append(int(l1[j]))
    else:
        lo.append(int(l1[j]))
le.sort()
lo.sort()
if (len(le) == 0):
    x = int(l1[4])
    while (x > 0):
        r = x % 10
        s += r
        x //= 10
    print(s)
elif (len(lo) == 0):
    x = int(l1[4])
    while (x > 0):
        c += 1
        x //= 10
    print(c)
else:
    print(int(le[0]) + int(lo[len(lo)-1]))