

def first__number_pattern():
    """ print: 
              1
              2 2
              3 3 3
              4 4 4 4
    """
    rows =  int(input("Enter rows: "))
    for i in range(rows):
        for j in range(i+1):
            print(i+1,end="")

        print()

first__number_pattern()
