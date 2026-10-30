"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a number entered by the user
# 2. Process: the program checks every number from 1 to N and determines whether it is odd or even
# 3. Out: each number with its result (odd or even)
# 4. What happens on 0, on a negative number, on a very large number: if the user enters 0 or a negative number, the program displays an error message. if the user enters 5000 or more, the program asks for a smaller number


# Your code below

number = int(input("Enter a number: "))

if number <= 0:
    print("Please enter a positive number")
elif number >= 5000:
    print("Please enter a number smaller than 5000")
else:
    for i in range (1, number + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")