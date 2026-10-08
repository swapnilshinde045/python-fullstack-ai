a = set(map(int, input("Enter elements of set a: ").split()))
b = set(map(int, input("Enter elements of set b: ").split()))

print(a | b)    # union
print(a & b)    # intersection
print(a - b)    # difference
print(a ^ b)    # symmetric difference

