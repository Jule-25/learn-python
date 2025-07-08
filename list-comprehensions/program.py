prizes = [5, 10, 50, 100, 1000]

dbi_prizes = []
for prize in prizes:
    dbi_prizes.append(prize * 2)

print(dbi_prizes)

# comprehension method
dbi_prizes = [prize * 2 for prize in prizes]
print(dbi_prizes)

#squaring of numbers
nums = [1, 2, 3, 4, 5, 6, 7]
squared_even_nums = []

for num in nums:
    if (num**2) % 2 == 0:
        squared_even_nums.append(num**2)
print(squared_even_nums)

# comprehension method
squared_even_nums = [num**2 for num in nums if (num**2) % 2 == 0]
print(squared_even_nums)