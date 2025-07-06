def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and i am a {val} belt')

ninja_belts = {}

while True:
    ninja_name = input('Enter name: ')
    ninja_belt = input('Enter belt color: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('Add another? (y/n)')
    if another == 'y':
        continue
    else:
        break

ninja_intro(ninja_belts)
