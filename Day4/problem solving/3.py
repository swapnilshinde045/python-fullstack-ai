#reverse a list in three ways: reverse(), slicing and a loop.

num = [1, 2, 3, 4, 5]

rev_slicing = num[::-1]
print("1. Slicing:", rev_slicing)

num_copy = num.copy()
num_copy.reverse()
print("2. reverse():", num_copy)

rev_loop = []
for i in range(len(num) - 1, -1, -1):
    rev_loop.append(num[i])
print("3. Loop:", rev_loop)
