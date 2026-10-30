"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a sentence entered by the user
# 2. Process: the program applies four different text transformations to the sentence
# 3. Out: four transformed version of the original sentence
# 4. My four transformations, and when each is useful: upper (all letters are converted to uppercase), lower (all letters are converted to lowercase), strip (spaces at the beginning and end are removed), title (the first letter of each word is capitalized)


# Your code below

sentence = input("Enter a sentence: ")

# upper

print("Uppercase: ", sentence.upper())

# lower

print("Lowercase: ", sentence.lower())

#strip

print("Without extra spaces: ", sentence.strip())

#title

print("Title case: ", sentence.title())