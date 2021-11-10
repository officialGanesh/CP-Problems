
# Factorial using for loop

def factorial_using_for_loop(n):
    """ Factorial using for loop """
    fact = 1

    for i in range(1,n+1):
        fact *= i

    return fact

#print(factorial_using_for_loop(5))

def factorial_using_while_loop(n):
    i,fact = 1,1
    while(i<=n):
        fact*=i
        i+=1
    return fact

#print(factorial_using_while_loop(100))

