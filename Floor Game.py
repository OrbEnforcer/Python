welcome = print("Welcome to Floor Game!\nRules are simple. You have 3 ways to ascend a floor - elevator, escalator and stairs.\nPoints for each are as follows-\nElevator(1) - Score increment to next even number.\nEscalator(2) - Score increment to next odd number.\nStairs(3) - Score increment to next prime number.") 
floors = int(input("How many floors are there in the building? "))
a = 0
pcount = 0
point = 0
elevator = 2
escalator = 1
stair = 2 
while (a < floors):
    ascend = int(input("Enter the facility to go to next floor: "))
    if (ascend == 1):
        point += elevator
        elevator += 2
    elif (ascend == 2):
        point += escalator
        escalator += 2
    elif (ascend == 3):
        for i in range (1,floors,1):
            if (stair % i == 0):
                pcount += 1                
            if (pcount == 1):
                stair = i 
        point += stair   
    else:
        print("Your choices are '1' for elevator, '2' for escalator and '3' for stair.")
    a += 1
print(point)