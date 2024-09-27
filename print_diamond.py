#write a code that prints a diamond shape * using odd number
def odd_integer():
    #for inputing odd number
    number = int(input("Please enter an odd number: "))
    #for checking if the number is odd
    if number % 2 != 0:
        return number #return the odd integer
    else:
        print("Invalid. Please enter an odd number ")
        return odd_integer() #for valid input
def print_diamond():
    number = odd_integer()#for getting the valid integer

    #for calculating the mid point of diamond
    mid = number // 2
    
    #for calculating the top of the diamond
    for i in range(mid + 1):
        print(' ' * (mid - i), end ='')
        print('*' * (2 * i + 1))
    
    #for calculating the bottom of the diamond
    for i in range(mid -1,-1,-1):
        print(' ' * (mid - i), end ='')
        print('*' * (2 * i + 1))

print_diamond()