"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user's university and years of study
# 2. Process: asking the user for two pieces of information and printing a sentence which combine them
# 3. Out: a sentence displaying the user's university and years of study
# 4. My two fields, and what I would do with them: university and years of study, i would use these informations to assess a candidate's academic background


# Your code below
university = input ("Which university do you attend ? ")
years = input ("How many years have you studied ? ")
print ("My university is", university)

if years == "1" :
    print("I have studied for " + years + " year.")
else:
    print("I have studied for " + years + " years.")

if years == "1" :
    print("I study at " + university + " and I have completed " + years + " year of study.")
else:
    print("I study at " + university + " and I have completed " + years + " years of study.")
