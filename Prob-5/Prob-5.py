# Module 3
#   Programming Assignment 4
#     Prob-5.py

# Robert Ballenger


def main():
    try:
        x = eval(2)
        print("x:", x)
    except TypeError:
        print("There was a TypeError, exiting")
        exit
    except:
        print("Honestly we're not really sure where we went wront here.")
        print()
        print("I can't continue with this farce! I couldn't help you as a computer, all is doomed.")
        print()
        print("I am the weakest link.")
        print()
        print("Goodbye.")
        exit


main()
