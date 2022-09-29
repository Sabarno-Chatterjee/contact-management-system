import random
import art

print(art.logo)

input("Type roll to cast the dice.\n").lower()
roll = random.randint(1,6)
print(roll)