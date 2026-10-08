#remove duplicates from a list without using set

nums = [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 10, 10]

unique_nums = []
for x in nums:
    if x not in unique_nums:
        unique_nums.append(x)
print("Without set:", unique_nums)
