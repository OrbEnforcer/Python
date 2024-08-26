import random

def main():
    x = random.randint(-100,100)

    equation =  (x**2) - 50 * 1045 * x - 1250
    
    while equation != 0:
        print(
            'Trying to find the root of the equation at ' + str(x)
        )
        print(
            'At ' + str(x) + ' value of the equation will be ' + str(equation)
        )
        x = random.randint(-100,100)
        equation = (x**2) - 50 * 1045 * x - 1250

        continue
        
main()

def solve():
    print(
            'Trying to find the root of the equation at ' + str(x)
        )
    print(
            'At ' + str(x) + ' the given equation will be zero!'
        )

solve()