import random

print("Welcome to number guessing game.Enter the range of numbers in the next line.")
n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))

i = (random.randint(n1,n2))
x = i
y = int(input("Guess number: "))
while (y != x):
    y = int(input("Guess number: "))
    if (y == x):
        
        print("You guessed it.The number was " + str(i), end = ".")
            