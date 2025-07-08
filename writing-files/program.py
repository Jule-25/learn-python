with open('writing-files/doc/file.txt', 'w') as write_file:
    write_file.write('Hello World!')

# Use 'a' to not overwrite write_file
with open('writing-files/doc/file.txt', 'a') as write_file:
    write_file.write('From Python')