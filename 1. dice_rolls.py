import random
dice = int(input("please enter how many dices to roll: "))
sum = 0
for d in range(dice):
    roll = random.randint(1,6)
    sum = sum + roll
print("The sum of the rolls is " + str(sum)