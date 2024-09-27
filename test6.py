from datetime import datetime
now = datetime.now()
print('24BDS0141\nTimestamp:',now.strftime("%H:%M:%S"))
n = int(input())
d, d2 = {}, {}  
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
average_rainfall = {city: round(d[city] / d2[city],2) for city in d}
result = sorted((city, avg) for city, avg in average_rainfall.items())
print(result)
