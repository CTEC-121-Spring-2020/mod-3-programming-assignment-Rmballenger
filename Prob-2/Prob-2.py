# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Robert Ballenger

'''
# Inputs: Asks user for Name, Hourly Wage, and Hours Worked.

# Process: Seperate overtime and regular time pay and calculate.
# Subtracting insurance and tax withholdings from total wages.
# Finding what take home pay will be.

# Outputs: Regular Wages, Overtime Wages, Total Wages, Tax withholdings
# insurance withholdings, and take home pay.
'''


def main():

    # To begin, I start by getting the users input on the three
    # questions given. Name, Wage, and Hours.
    personsName = str(input("What is your name?\n"))
    personsWage = float(input("What is your hourly wage?\n"))
    personsHours = float(input("How many hours did you work?\n"))
    print("\n\n")

    # Here I check to see if the user has more than or equal to 40 hours
    # If they do, I find three new variables: extraTime (How many hours
    # over 40 the user is), overTime (Multiplying the overtime wage of
    # 1.5 by the persons wages, then by the hours over 40 that they were),
    # and regularTime (hours worked minus the hours over 40 times the
    #  normal wage.)
    if personsHours >= 40:
        extraTime = (personsHours - 40)
        overTime = extraTime*(personsWage*1.5)
        regularTime = (personsHours - extraTime)*(personsWage)

    # If they DON'T have more than 40 hours, it sends the function here.
    # overtime gets default set to 0 and regularTime is applied as normal
    # with their wage multiplied by their hours.
    else:
        overTime = 0.0
        regularTime = (personsWage * personsHours)

    # Next up is to find what the total wages will be, this is just
    # overtime plus regulartime pay. This is why I set overTime to 0
    # in the else statement. Also totalWages has now become a variable.
    totalWages = overTime + regularTime

    # I make taxWithholding a variable and calculate it by multiplying
    # the totalWages variable by .20 or 20%
    taxWithholding = totalWages*.20

    # I follow a similar pattern for insurance withholdings.
    insurWithholding = totalWages*.10

    # To find total take home pay, I can subtract both withholdings
    # from the totalWages found earlier.
    takehomePay = totalWages - (taxWithholding + insurWithholding)

    # Last step is to format the information.
    print("Your name is: ", personsName)
    print("Regular time is: ", regularTime)
    print("Overtime is: ", overTime)
    print("Total wages are: ", totalWages)
    print("Your Tax withholdings are: ", taxWithholding)
    print("Your Insurance withholdings are: ", insurWithholding)
    print("Your take home pay is: ", takehomePay)


main()
