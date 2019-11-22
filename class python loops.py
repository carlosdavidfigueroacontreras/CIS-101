import random

a = 0
b = 10
c = 6

for i in range(a,c):
    x = random.randint(a,b)
    print(x)

    if x == 5:
        print("middle")

    elif x == 1:
        print("lowest")

    elif x == 10:
        print("HIGHEST")

    elif x >= 8:
        print("larger in range")

    elif x<=3:
        print("perrin")

    else:
        print("nada mamaguevo")
        
    
