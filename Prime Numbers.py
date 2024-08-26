while True:    
    n = int(input("Enter number: "))
    c = 0
    for i in range (1,n):
        if (n % i == 0):
            c = c + 1
            i = i + 1
    if (c > 1):
        print("The number is composite.")
    else:
        print("The number is prime.")