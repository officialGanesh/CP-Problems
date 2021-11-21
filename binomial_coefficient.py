
def fact(num):
    "Find factorial of a given number"

    if( num == 0):
        return 1
    return num * fact(num-1)

def binomial_coeff():
    "Return the binomial coefficient.Using n!/r!(n-r)!"

    n = int(input("Enter value of n: "))
    r = int(input("Enter value of r: "))

    bino_coeff = fact(n)/fact(r)*fact(n-r)
    return bino_coeff

print(binomial_coeff())


