def is_even (n):
    return n%2 == 0

def factorial (n):
    result =1
    for i in range (1, n+1):
        result*=i
    return result

print (is_even(8))  #true
print (factorial(5))  #120