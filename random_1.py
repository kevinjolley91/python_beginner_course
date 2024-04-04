import random

print(random.randint(1,10))

print(random.random())

# Make your own version of a magic 8 ball that prints yes, no, or maybe each time you ask it

number = random.randint(1,3)

if number == 1:
    print("yes")
elif number == 2:
    print("no")
else:
    print("maybe")