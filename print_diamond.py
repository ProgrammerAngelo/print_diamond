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
#method for looping that says"Please provide an odd integer"