a=int(input("enter value of a : "))
b=int(input("enter value of b : "))

def min_max(a, b):
    return min(a,b),max(a,b)

Low, High = min_max(a,b)
print("The low value is :", Low)
print("The High value is :", High)