# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Robert Ballenger


def shippingCost(orderSubTotal):

    shippingCost = 2.99

    # To start, I run a basic if/else statement that checks if the
    # orderSubTotal variables value is greater than or equal to the
    # float value of 10.00. If true, I have the program change the
    # value of shippingCost to 0.00 (I changed it to a string for
    # dramatic flair).  If false, shippingCost stays at 2.99.
    # Either result, it prints a string and then shippingCost.

    if orderSubTotal >= 10.00:
        shippingCost = "Zero!"
        print("Your shipping cost will be", shippingCost)
    else:
        print("Your shipping cost will be", shippingCost)

    return shippingCost


def unitTest():
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(5.99))
    print()
    # To start I wanted to cover all possible fail points, including
    # being over 10.00, and JUST under, and 10.00 exactly.)
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(9.99))
    print()
    print("Shipping cost if subtotal > 10.00:\t", shippingCost(11.00))
    print()
    print("Shipping cost if subtotal = 10.00:\t", shippingCost(10.00))


if __name__ == "__main__":
    unitTest()
