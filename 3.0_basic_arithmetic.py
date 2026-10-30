"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two numbers entered by the user
# 2. Process: thr program calculates the addition, substraction, multiplication and division of the two numbers
# 3. Out:the results of the four mathematical operations
# 4. What happens when the second number is zero, and why: the program displays a message instead of performing the division because division by zero is mathematically impossible


# Your code below
number_1 = int(input ("Choose a number : "))
number_2 = int(input ("Choose a second number : "))

print ("The number 1 is : ", number_1)
print ("The number 2 is : ", number_2)

#Addition 
sum = number_1 + number_2
print ("The sum of the two numbers is: ", sum)

#Substraction
dif = number_1 - number_2
print ("The difference between the two numbers is: ", dif)

#Product
prod = number_1 * number_2
print ("The product of the two numbers is: ", prod)

#Division
if number_2 != 0 : 
    div = number_1 / number_2
    print ("The division result is ", div)

else :
    print ("Division by zero is not possible")

print(7/2)
print(7//2)