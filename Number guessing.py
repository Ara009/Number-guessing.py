import random
import math

lower = int(input("Enter the lower bound:-"))
upper = int(input("Enter the upper bound:-"))

x = random.randint(lower,upper)
print("\nYou'hv only",round(math.log(upper-lower,1+2)),"chances to guess the interger!\n")

count = 0
while count < math.log(upper-lower,1+2):
    count+=1
    guess = int(input("Guess a number:-"))

    if x == guess:
        print("Congratualtion you did it in",count,"try")
        break

    elif x > guess:
        print("You guess too small!")

    elif x < guess:
        print("You guess too high")

    if count >= math.log(upper-lower,1+2):
        print("\nThe number is %d" % x)
        print("\tBetter luck next time!")