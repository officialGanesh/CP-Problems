

def first__number_pattern():
    """ print: 
              1
              1 2
              1 2 3
              1 2 3 4
    """
    rows =  int(input("Enter rows: "))
    for i in range(rows):
        for j in range(i+1):
            print(j+1,end="")

        print()

first__number_pattern()
