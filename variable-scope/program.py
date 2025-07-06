my_name = 'Jule' # my_name is a global variable

def print_name():
    global my_name   # Overriding the global scope
    my_name = 'Oumar' # my_name now has a local scope
    print('the name inside the function is', my_name) 

print_name() # Gonna print 'Oumar'
print('outside the function the name is', my_name) # Gonna print 'Oumar'