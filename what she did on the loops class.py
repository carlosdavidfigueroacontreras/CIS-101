import random
a = 0
b = 15
c = 5
x = random.randint(a,b)
y = int(input('How many people did your son invite?:'))

food = ["turkey", "apple pie", "mac and cheesse"]

total = c + x + y

answer = "n"

while answer != "y":
    for item in food:
        print("we need " + str(total) + " " + item)
    answer = input ("do you want to keep goung? type y to exit:")
    

