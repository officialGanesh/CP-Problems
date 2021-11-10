

def factorial_using_recursion(n):
    """ Factorial using recursion"""
    if( n==0 or n==1 ):
        return 1
    return n * factorial_using_recursion(n-1)

#print(factorial_using_recursion(100))