

def stringPalindrome():
    " String palindrome "

    user_input = input("Enter your data: \n")
    reversed_user_input = user_input[::-1]
    
    print(f"{user_input} is a palindrome ✔️") if (user_input==reversed_user_input) else print(f"{user_input} is not a palindrome ❎")
        

#stringPalindrome()

def numberPalindrome():
    " Number palindrome "

    data = eval(input("Enter any positive number: \n"))
    reverse = 0
    temp = data
    while(temp>0):
        remainder = temp%10 
        temp  = int(temp/10)
        reverse = (reverse*10)  + remainder
    
    print(f"{data} is a palindrome ✔️") if (data==reverse) else print(f"{data} is not a palindrome ❎")
        

#numberPalindrome()