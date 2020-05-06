# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Robert Ballenger


def letterGrade(score):
    # your code here

    if score == 5:
        grade = "A"
    elif score == 4:
        grade = "B"
    elif score == 3:
        grade = "C"
    elif score == 2:
        grade = "D"
    else:
        grade = "F"

    return grade


def unitTest():
    for score in range(6):
        print("Your score was", score, "so your grade is",
              letterGrade(score), "\n")
    # your test code here


if __name__ == "__main__":
    unitTest()
