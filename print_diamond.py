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
    number = odd_integer()

    mid = number // 2
    
    for i in range(mid + 1):
        print(' ' * (mid - i), end ='')
        print('*' * (2 * i + 1))

    for i in range(mid -1,-1,-1):
        print(' ' * (mid - i), end ='')
        print('*' * (2 * i + 1))

print_diamond()
#method for looping that says"Please provide an odd integer"