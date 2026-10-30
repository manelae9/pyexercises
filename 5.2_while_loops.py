"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: answers entered by the user (yes or no)
# 2. Process:the program asks the user whether they want to continue, until they answer no or reach the maximum number of attempts
# 3. Out: a summary showing the number of attempts and whether the user chose to stop
# 4. My stop condition, my attempt limit, my summary: the program stops when the user answers no, the maximum number of attempts is 5, the summary contains the number of attempts and the final result


# Your code below
i = 0
answer = ""

while i < 5 and answer != "no":
    answer = input("Do you want to continue ? (yes/no): ").lower().strip()
    i += 1

    if answer == "yes":
        print("You chose to continue.")
    elif answer == "no":
        print("You chose to stop.")
    else:
        print("Invalid input.")

print("Summary:")
print("Number of attempts:", i)

if answer == "no":
    print("You chose to stop.")
else:
    print("Maximum number of attempts reached.")
