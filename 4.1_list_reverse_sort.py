"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of monthly marketing campaign budgets in euro
# 2. Process: he program displays the budgets in four different orders
# 3. Out: the budgets in different orders and the original list at the end
# 4. My four orders, and which ones modify the original: I choose the original order, ascending order, descending order and random order


# Your code below

import random

budgets = [1200, 800, 1500, 1080, 2000, 720, 1300, 1500, 2740]

# Original order
print("Original order: ", budgets)

# Ascending order
ascending = sorted(budgets)
print("Ascending order: ", ascending)

# Descending order 
descending = sorted(budgets, reverse=True)
print("Descending order: ", descending)

# Random order
random_order = random.sample(budgets, len(budgets))
print("Random order: ", random_order)

# Display the original list to check it has not changed
print("original list at the end: ", budgets)