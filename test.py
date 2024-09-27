i = 0
n1 = int(input())
x = n1
y = n1
even = 0
odd = 0
sum5 = 0
count = 0
while(i < 4):
    n = int(input())
    if (n % 2 == 0):
        even += 1
        if (x > n):
            x = n 
    else:
        odd += 1
        if (y < n):
            y = n
    i += 1
    if (i == 4):
        num5 = n 
if (odd == 0):
    while (num5 > 0):
        r = num5 % 10
        num5 //= 10
        sum5 += r
    print(sum5)
elif (even == 0):
    while (num5 > 0):
        num5 //= 10
        count += 1
    print(count)
else:
    print(x + y)

'''	
151
171
183
201
111
131
141
161
153
233
'''