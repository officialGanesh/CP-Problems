

def collatz_sequence(num):
    """ The simplest impossible math problem 🚀"""

    while (num!=1):
        if(num%2==0):
            num = int(num//2)
            print(num)
        elif(num%2!=0):
            num = (num)*3+1
            print(num)
        else:
            return 1

collatz_sequence(3)
