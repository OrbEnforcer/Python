n = int(input())
val = [1000, 500, 100, 50, 10, 5, 1]
roman = ["m", "d", "c", "l", "x", "v", "i"]
i = 0
while n > 0:
    for j in range(n // val[i]):
        print(roman[i])
        n -= val[i]
    i += 1