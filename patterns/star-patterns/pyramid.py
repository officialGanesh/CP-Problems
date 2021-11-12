

def pyramid_triangle_1():

    rows = int(input("Enter rows: "))
    for i in range(rows):
        print(" "*(rows-i) + "* "*(i+1))
    
#pyramid_triangle_1()


def pyramid_triangle_2():

    rows = int(input("Enter rows: "))
    for i in range(rows):
        print("  "*(rows-i-1) + "* "*((2*i)+1))
    
pyramid_triangle_2()


