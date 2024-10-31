import csv
import random

names = []

with open("names.csv", newline="") as infile, open("output.csv", "a+", newline="") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)
    for row in reader:
      names.append(row["name"])

print("loaded " + str(len(names)) + " names to pair!")
print("Please assert that there are even number of names.")

pairs = []

while len(names) > 0:
  id1 = random.randrange(0, len(names))
  name1 = names.pop(id1)
  id2 = random.randrange(0, len(names))
  name2 = names.pop(id2)
  pairs.append((name1, name2))

print("Pairing done, " + str(len(pairs)) + " pairs created!")
print("")
print("Generating message to copy to Slack: ")
for pair in pairs:
  print("@" + pair[0] + "\t -- \t@" + pair[1])