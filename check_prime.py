from math import sqrt,floor

def primeNumber(number):
    """ Return true if number is prime. Otherwise, return false"""
    
    if number == 1:
        return False
    max_value = floor(sqrt(number))
    for i in range(2,max_value+1):
        if(number%i==0):
            return False
    return True

for k in range(1,101):
    # Check for 100 numbers
    print(f"{k}: {primeNumber(k)}")

