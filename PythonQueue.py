import random
firstNames = ["alex", "donald", "richard", "edward", "larry", "patrick", "sandy", "jay", "danny", "brian"]
names = []

for item in range(0,10):
    names.append(random.choice(firstNames))
for item in range(0, len(names)):
    print(names.pop(0))

