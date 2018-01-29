# LOOPS AND RANDOM NUMBERS

# FOR LOOPS

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(-5, 5):
    print(i)

for i in range(5, 15, 3):
    print(i)

# RANDOM NUMBERS
import random

print(random.randrange(10))  # random 0 to 9
print(random.randrange(5, 16)) # 5 to 15
print(random.randrange(-5, 5)) # -5 to 4
print(random.randrange(5, 15, 3)) # 5 to 14 by 3s (5, 8, 11, 14)
print(random.randrange(10, -11, -2))

print(random.random()) # random FLOAT from 0 to 1
print(random.random() * 10 + 5) # random FLOAT from 5 to 15

# BREAK
# keep rolling a die until you get a 6
for i in range(100):
    roll = random.randrange(1, 7)
    print("You rolled a ", roll, "on roll number", i)
    if roll == 6:
        break

# CONTINUE
for i in range(10):
    roll = random.randrange(1, 7)
    if roll % 2:
        continue
    print(roll)

# FOR ELSE
# if you make it all the way through the FOR loop without breaking
# then you do the ELSE statement

for i in range(10):
    n = random.radnrange(10)
    if n == 0:
        break
else:
    print("Did not roll zero")