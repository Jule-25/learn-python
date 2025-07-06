# Iterate through the range numbers 
for n in range(5): # range(5) eq [0, 1, 2, 3, 4]
    print(n)

print("") # separating the outputs

# Iterate through the range [3, 4, 5, 6, 7, 8, 9]
for n in range(3, 10):
    print(n)

print("")

# Iterate through the numbers 0 to 20 at a pace of 4
for n in range(0, 20, 4):
    print(n)

print("")

names = ['Oumar', 'Ibou', 'Badar']

# Iterate through the numbers starting from 0 to the length of names
for n in range(len(names)):
    print(n)

print("")

# Do backward iteration
for n in range(len(names) - 1, -1, -1):
    print(n)