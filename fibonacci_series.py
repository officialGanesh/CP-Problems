
def fibonacci_series(n):
    """ **** Fibonacci series using recursion ****
    first and second term of this series are 0 and 1 respectively.And remaining terms are formed using general pattern
    by adding two previous terms"""

    a,b = 0,1
    if(n==0):
        return a
    elif(n==1):
        return b
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)

for i in range(10): # first ten fibonacci series terms
    print(f"{fibonacci_series(i)} ",end="")


    