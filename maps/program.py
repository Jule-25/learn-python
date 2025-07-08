from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return " ".join(anagram)


words = ['beetroot', 'carrots', 'patatoes']
anagrams = []

for word in words:
    anagrams.append(jumble(word))

print(anagrams)

# map method
anagrams = list(map(jumble, words))
print(anagrams)

#list comprehension
anagrams = [jumble(word) for word in words]
print(anagrams)