

def find_greatest_number():
    """ to determine the greatest of three numbers """

    a,b,c = int(input("Enter first number: ")),int(input("Enter second number: ")),int(input("Enter third number: ")),

    if(a>b):
        if(a>c):
            print(f"{a} is the greatest among {a,b,c}")
        else:
            print(f"{c} is the greatest among {a,b,c}")
    else:
        if(b>c):
            print(f"{b} is the greatest among {a,b,c}")
        else:
            print(f"{c} is the greatest among {a,b,c}")

find_greatest_number()
