

def right_shape_triangle():

    rows = int(input("Enter rows: "))

    for i in range(rows):
        print("  "*(rows-i) + "* "*(i+1))

right_shape_triangle()