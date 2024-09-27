n = eval(input())
target = int(input())
for i in n:
    for j in n:
        if (i + j == target):
            l1 = [n.index(i),n.index(j)]
print(l1)