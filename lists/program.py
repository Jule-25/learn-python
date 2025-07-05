words = ['Hi', 'My', 'Name', 'Is', 'Jule']

# Printing the first element in the list
print(words[0]) # 'Hi'

# Printing the last element in the list
print(words[-1]) # 'Jule'

# Contatenating lists
words2  = ['How', 'About', 'You']
print(words + words2) 

# Appending an element at the end of a list
words2.append('?') # ['How', 'About', 'You', '?']
print(words2)

# Removing an element from a list
words2.remove('?')
print(words2) # ['How', 'About', 'You', '?']

# Nesting lists
nums = [[2, 3, 5], [6, 7, 8], [9, 10, 11]]

# Printing the first list
print(nums[0]) # [2, 3, 5]