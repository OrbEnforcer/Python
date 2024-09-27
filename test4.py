n = int(input())
d,d2,l1,l2 = {},{},[],[]
s = 1
for i in range(n):
    main = input()
    m_split = main.split(' ')
    city = m_split[0]
    rainfall = float(m_split[1])
    if city in d: 
        d[city] += rainfall
        d2[city] += 1
    else:
        d[city] = rainfall
        d2[city] = 1
avg = {city: round(d[city] / d2[city],2) for city in d}
for city in avg:
    l1.append(city)
x = sorted(l1)
print(x)
for x in avg:
    l2.append(tuple((str8(x),d[x])))
print(avg)