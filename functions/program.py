# Define a function called greet()
def greet():
    print('Hello World')

# Invoke the function
greet()

# Define a function with parameters
def print_user_info(name, age):
    print(f'Your name is {name}')
    print(f'You are {age} years old.')

# Invoke the function passing in the arguments
print_user_info('Jule', 20)

# Define a function with default parameters
def print_user_name(name = 'Jule'):
    print(name)

# Invoke the function passing in no arguments
print_user_name()

# Invoke the function this time with an argument
name = input('Enter your name: ')
print_user_name(name)



