nums = [1, 2, 3, 4, 5, 6]

def double_num(num):
    return num * 2

nums_doubled = list(map(lambda n: n * 2, nums))

print(nums_doubled)