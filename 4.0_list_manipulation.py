"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of monthly marketing campaign budgets in euros
# 2. Process: the program display the list, selects one budget, sort the budgets and calculates their average
# 3. Out: the original list, one selected budget, the sorted list and the average budget
# 4. What my list is about, and what I computed from it: it contains the bidgets of eight marketing campaigns, i calculated the average budget to comprae campaign sepnding and understand how much is allocated to each campaign on average


# Your code below

budgets = [1200, 800, 1500, 1080, 2000, 720, 1300, 1500, 2740]

# display the whole list
print("Marketing campaign budgets: ", budgets)

# display one item
print("The sixth campaign budget is: ", budgets[5])

# display the sorted list
sorted_budgets = sorted(budgets)
print("Sorted budgets",sorted_budgets)

# calculate the average
average = sum(budgets) / len(budgets)
print("The average campaign budget is:", average)

# remove last item
budgets.pop()
print("List after removing last item: ", budgets)

