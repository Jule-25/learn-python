#ipsum_file = open('reading-files/doc/file.txt')

# Iterating through the lines in the file
#for line in ipsum_file:
#   print(line.rstrip())

#ipsum_file.seek(0)
#lines = ipsum_file.readlines()
#print(lines)

#ipsum_file.close()

with open('reading-files/doc/file.txt') as a_file:
    lines = a_file.readlines()

print(lines)