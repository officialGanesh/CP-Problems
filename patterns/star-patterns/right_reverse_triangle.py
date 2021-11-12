

def right_reverse_shape_triangle():

    rows = int(input("Enter rows: "))

    for i in range(rows):
        print("  "*(i) + "* "*(rows-i))
    
right_reverse_shape_triangle()