

def first__number_pattern():
    """ print: 
              1
              2 3
              4 5 6
              7 8 9 10
    """
    rows =  int(input("Enter rows: "))
    k = 1
    for i in range(rows):
        for j in range(i+1):
            print(k,end="")
            k+=1

        print()

first__number_pattern()
