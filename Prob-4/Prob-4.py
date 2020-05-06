# Module 3
#   Programming Assignment 4
#     Prob-4.py

# Robert Ballenger

# Author: Bruce Elgort
# Date: July 12, 2017

"""
The Elgorte coffee shop sells coffee at $16.50 a pound
plus the cost of shipping. Each order ships for $0.76
per pound plus $1.25 fixed cost for overhead. If the
number of pounds of the coffee order exceeds 10, then
the shipping cost is waived. Write a program that
calculates the cost of an order. Name your function
coffeeProcessor()
"""

def coffeeProcessor():

    #------------------------------------------------------------------------------------------------
    # Defining the Variables. It was done correctly.
    '''
    # define variables
    overHead = 1.25
    priceOfCoffee = 16.50
    '''
    overHead = 1.25
    priceOfCoffee = 16.50

    #------------------------------------------------------------------------------------------------
    # Getting the number from the user again. I changed the evaluate function to a float for two
    # reasons, the first was because the input  may be a decimal, and because theres no evaluation
    # going on in the input, I also added a \n so the user has a new line to input their number(s).
    '''
    # get number of pounds from user
    quantity = evaluate(input("How many pounds of coffee would you like to order?")
    '''
    quantity = float(input("How many pounds of coffee would you like to order?\n"))

    #------------------------------------------------------------------------------------------------
    # Using an if/else statement, I check the quantity ordered and depending on 
    # if true or false, it assigns a new variable with a value of either .76 or 0.
    # the original assignment was missing a : after the 10
    '''
    # Check number of pounds ordered
    # If less than or equal to 10 pounds we must charge for shipping
    if quantity <= 10
        shippingPerPound = .76
    else
        shippingPerPound = 0     
    '''
    if quantity <= 10:
        shippingPerPound = .76
    else:
        shippingPerPound = 0

    #------------------------------------------------------------------------------------------------
    # On this step, I do the basic math functions but instead of doing them all on one line like
    # the example did, I split the two parts of the equation into seperate variables.
    costOfShipping = (shippingPerPound * quantity)
    costBeforeShipping = (quantity * priceOfCoffee)

    #------------------------------------------------------------------------------------------------
    # Using these variables, I can Calculate the cost in a neater looking line of code.
    '''
    # Calculate cost of order
    costOfOrder = (quantity * priceOfCoffee) + (quntity * shippingPerPound) + overHead
    '''
    costOfOrder = costBeforeShipping + costOfShipping + overHead

    #------------------------------------------------------------------------------------------------    
    # Here I used the variables I created earlier to do some checks when running the code initially.
    # I commented it out but left it here as a 'showing your work' kind of thing.
    '''
    print("The quantity is:", quantity)
    print("The shipping PerPound is:", shippingPerPound)
    print("The cost before shipping:", costBeforeShipping)
    print("The cost of shipping is:", costOfShipping)
    '''

    #------------------------------------------------------------------------------------------------
    # Last but not least, we have the print command to show the final cost of order to the user.
    # I added a space after the comma, but mainly for asthetic reasons.
    '''
    # Print result
    print(The cost of the order is:",costOfOrder)
    '''
    print("The cost of the order is:", costOfOrder)

#-----------------------------------------------------------------------------------------------------
# There isn't a 'go' in front of the function name. Fixed.    
'''
# start the program
gocoffeeProcessor()
'''
coffeeProcessor()